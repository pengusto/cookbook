import importlib.util
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

spec = importlib.util.spec_from_file_location('cookbook', Path(__file__).resolve().parents[1] / 'scripts/cookbook.py')
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


class PackagingContracts(unittest.TestCase):
    def test_store_metadata_and_safe_square_icons_are_packaged(self):
        import xml.etree.ElementTree as ET
        import struct
        for host in ('codex', 'claude'):
            _, files = app.plugin_files(host)
            manifest = json.loads(files[f'.{host}-plugin/plugin.json'])
            if host == 'codex':
                self.assertIs(manifest.get('requires_local_executor'), True)
            else:
                self.assertNotIn('requires_local_executor', manifest)
            listing = manifest['interface'] if host == 'codex' else manifest
            keys = ('logo', 'composerIcon', 'logoDark', 'composerIconDark') if host == 'codex' else ('icon',)
            for key in keys:
                self.assertIn(listing[key][2:], files)
            for name in ('icon.svg', 'icon-dark.svg'):
                raw = files[f'assets/{name}']
                svg = ET.fromstring(raw)
                self.assertEqual(svg.attrib['viewBox'], '0 0 512 512')
                self.assertLess(len(raw), 5 * 1024 * 1024)
                self.assertFalse(any(node.tag.rsplit('}', 1)[-1] in ('script', 'image', 'foreignObject') for node in svg.iter()))
                self.assertNotIn(b'href=', raw)
                png = files[f'assets/{name.replace(".svg", ".png")}']
                self.assertEqual(png[:8], b'\x89PNG\r\n\x1a\n')
                self.assertEqual(struct.unpack('>II', png[16:24]), (512, 512))
                self.assertLess(len(png), 5 * 1024 * 1024)
            if host == 'codex':
                self.assertLessEqual(len(listing['displayName']), 30)
                self.assertLessEqual(len(listing['shortDescription']), 30)
                self.assertLessEqual(len(listing['longDescription']), 4000)
                self.assertTrue(all(len(p) <= 128 for p in listing['defaultPrompt']))

    def test_deterministic_and_complete_archives(self):
        for row in app.catalog():
            if row['status'] != 'source':
                continue
            first, second = io.BytesIO(), io.BytesIO()
            app.zip_bytes(row, first)
            app.zip_bytes(row, second)
            self.assertEqual(first.getvalue(), second.getvalue())
            with zipfile.ZipFile(first) as archive, tempfile.TemporaryDirectory() as destination:
                archive.extractall(destination)
                slug, rendered = app.rendered_files(row, 'plain')
                installed = Path(destination) / slug
                self.assertEqual({str(p.relative_to(installed)) for p in installed.rglob('*') if p.is_file()}, set(row['files']))
                for name, digest in row['files'].items():
                    self.assertEqual((installed / name).read_bytes(), rendered[name])

    def test_install_refuses_replacement_and_dangling_symlink(self):
        with tempfile.TemporaryDirectory() as directory:
            dest = Path(directory)
            app.install('let-them-see-it', dest)
            marker = dest / 'am-i-ready-to-share/user-note'
            marker.write_text('preserve')
            with self.assertRaises(ValueError):
                app.install('let-them-see-it', dest)
            self.assertEqual(marker.read_text(), 'preserve')
            (dest / 'did-i-leak').symlink_to(dest / 'absent')
            with self.assertRaises(ValueError):
                app.install('did-i-leak', dest)

    def test_unlicensed_candidate_is_not_installable(self):
        with tempfile.TemporaryDirectory() as directory:
            from unittest.mock import patch
            with patch.object(app, 'catalog', return_value=[{'id': 'unlicensed-candidate', 'status': 'candidate'}]), self.assertRaises(ValueError):
                app.install('unlicensed-candidate', Path(directory))
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_tampered_hash_and_unsafe_paths_are_rejected(self):
        row = json.loads(json.dumps(next(r for r in app.catalog() if r['status'] == 'source')))
        row['files']['SKILL.md'] = '0' * 64
        with self.assertRaises(ValueError):
            app.package_files(row)
        row['files'] = {'../outside': '0' * 64, 'SKILL.md': '0' * 64, 'LICENSE': '0' * 64}
        with self.assertRaises(ValueError):
            app.package_files(row)

    def test_plugin_archives_preserve_exact_skills_and_hidden_manifests(self):
        payloads = {}
        for host in ('codex', 'claude'):
            config, files = app.plugin_files(host)
            payloads[host] = {name: data for name, data in files.items() if name.startswith('skills/')}
            self.assertIn('skills/am-i-making-progress/SKILL.md', files)
            for row in app.catalog():
                if row['id'] not in config['skills']:
                    continue
                slug, rendered = app.rendered_files(row, 'plain')
                for name, content in rendered.items():
                    self.assertEqual(files[f'skills/{slug}/{name}'], content)
            for key in ('hooks', 'mcpServers', 'dependencies'):
                self.assertNotIn(key, json.loads(files[f'.{host}-plugin/plugin.json']))
            first, second = io.BytesIO(), io.BytesIO()
            archive_files = {f'{config["name"]}/{name}': data for name, data in files.items()}
            app.write_zip(archive_files, first)
            app.write_zip(archive_files, second)
            self.assertEqual(first.getvalue(), second.getvalue())
            with zipfile.ZipFile(first) as archive, tempfile.TemporaryDirectory() as directory:
                archive.extractall(directory)
                root = Path(directory) / config['name']
                self.assertEqual({str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}, set(files))
                self.assertEqual(json.loads((root / f'.{host}-plugin/plugin.json').read_text())['name'], config['name'])
                for name, data in files.items():
                    self.assertEqual((root / name).read_bytes(), data)
        self.assertEqual(payloads['codex'], payloads['claude'])

    def test_marketplaces_resolve_from_marketplace_root(self):
        for host in ('codex', 'claude'):
            config, _ = app.plugin_files(host)
            path, value = app.marketplace(host, config)
            entry = value['plugins'][0]
            source = entry['source']['path'] if host == 'codex' else entry['source']
            self.assertTrue(source.startswith('./plugins/'))
            self.assertNotIn('..', Path(source).parts)
            manifest = app.ROOT / 'dist' / 'plain' / host / source / f'.{host}-plugin/plugin.json'
            self.assertTrue(manifest.is_file())
            self.assertEqual(entry['name'], json.loads(manifest.read_text())['name'])

    def test_bundle_rejects_unlicensed_or_missing_selection(self):
        from unittest.mock import patch
        original = Path.read_text
        config = json.loads((app.ROOT / 'bundle.json').read_text())
        for selected in (['unlicensed-candidate'], ['absent'], ['did-i-leak', 'did-i-leak']):
            config['skills'] = selected
            def read(path, *args, **kwargs):
                return json.dumps(config) if path == app.ROOT / 'bundle.json' else original(path, *args, **kwargs)
            rows = app.catalog() + [{'id': 'unlicensed-candidate', 'status': 'candidate'}]
            with patch.object(app, 'catalog', return_value=rows), patch.object(Path, 'read_text', read), self.assertRaises(ValueError):
                app.plugin_files('codex')

    def test_variants_share_workflows_but_never_display_both_names(self):
        for row in app.catalog():
            outputs = {}
            for variant in app.VARIANTS:
                slug, files = app.rendered_files(row, variant)
                title = row['title'] if variant == 'plain' else row['cooking_title']
                other = row['cooking_title'] if variant == 'plain' else row['title']
                self.assertIn(('name: '+slug+'\n').encode(), files['SKILL.md'])
                self.assertIn(('# '+title+'\n').encode(), files['SKILL.md'])
                self.assertIn(('display_name: "'+title+'"').encode(), files['agents/openai.yaml'])
                self.assertNotIn(other.encode(), files['agents/openai.yaml'])
                self.assertNotIn(b'{{', files['SKILL.md'])
                import re
                normalized = {}
                for name, content in files.items():
                    if name in ('SKILL.md', 'agents/openai.yaml'):
                        content = content.replace(('name: '+slug+'\n').encode(), b'name: ID\n')
                        content = content.replace(('$'+slug).encode(), b'$ID')
                        if name == 'SKILL.md':
                            content = content.replace(('# '+title+'\n').encode(), b'# TITLE\n')
                            content = content.replace(('description: '+title).encode(), b'description: TITLE')
                        else:
                            content = content.replace(('display_name: "'+title+'"').encode(), b'display_name: "TITLE"')
                    normalized[name] = content
                outputs[variant] = normalized
            self.assertEqual(outputs['plain'], outputs['kitchen'])

    def test_cross_variant_single_install_is_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            dest = Path(directory)
            app.install('kill-the-todos', dest, 'plain')
            with self.assertRaises(ValueError):
                app.install('kill-the-todos', dest, 'kitchen')
            self.assertTrue((dest / 'can-we-finish/SKILL.md').is_file())

    def test_alternative_plugins_use_same_identity(self):
        for host in ('codex','claude'):
            plain, _ = app.plugin_files(host, 'plain')
            kitchen, _ = app.plugin_files(host, 'kitchen')
            self.assertEqual(plain['name'], kitchen['name'])
            self.assertEqual(app.marketplace(host, plain), app.marketplace(host, kitchen))


if __name__ == '__main__':
    unittest.main()
