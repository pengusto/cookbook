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
    def test_store_uploads_contain_plugin_at_root_without_marketplace_or_sidebar(self):
        for variant in app.VARIANTS:
            config, files = app.plugin_files('codex', variant)
            upload = app.ROOT / 'dist/store' / variant / f'{config["name"]}.zip'
            with self.subTest(variant=variant), zipfile.ZipFile(upload) as archive:
                self.assertEqual({name: archive.read(name) for name in archive.namelist()}, files)
                self.assertIn('.codex-plugin/plugin.json', archive.namelist())
                self.assertNotIn('.mcp.json', archive.namelist())
                self.assertFalse(any('marketplace.json' in name for name in archive.namelist()))

    def test_package_readmes_show_only_selected_names_and_host_invocations(self):
        for host in ('codex', 'claude'):
            for variant in app.VARIANTS:
                config, files = app.plugin_files(host, variant)
                for name in ('README.md', 'README.de.md'):
                    text = files[name].decode()
                    self.assertIn(config['version'], text)
                    self.assertNotIn('{{', text)
                    for row in app.catalog():
                        title = row['title'] if variant == 'plain' else row['cooking_title']
                        other = row['cooking_title'] if variant == 'plain' else row['title']
                        slug = row['install_ids'][variant]
                        command = f'${slug}' if host == 'codex' else f'/{config["name"]}:{slug}'
                        self.assertIn(f'| {title} | `{command}` |', text)
                        self.assertNotIn(other, text)

    def test_both_hosts_and_variants_include_every_reviewed_source(self):
        reviewed = {row['id']: row for row in app.catalog() if row['status'] == 'source'}
        for host in ('codex', 'claude'):
            for variant in app.VARIANTS:
                with self.subTest(host=host, variant=variant):
                    config, files = app.plugin_files(host, variant)
                    self.assertEqual(set(config['skills']), set(reviewed))
                    provenance = json.loads(files['SOURCES.json'])
                    self.assertEqual({row['id'] for row in provenance['skills']}, set(reviewed))
                    for row in reviewed.values():
                        slug, _ = app.rendered_files(row, variant)
                        self.assertIn(f'skills/{slug}/LICENSE', files)

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
                source_listing = json.loads((app.ROOT / 'store/listing.json').read_text())
                self.assertEqual(listing['shortDescription'], source_listing['shortDescription'])
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
                    if name in ('SKILL.md', 'agents/openai.yaml', 'examples.md'):
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

    def test_download_zips_are_self_contained_marketplaces(self):
        for variant in ('plain', 'kitchen'):
            for host in ('codex', 'claude'):
                with self.subTest(variant=variant, host=host):
                    config, files = app.plugin_files(host, variant)
                    market_path, market = app.marketplace(host, config)
                    with zipfile.ZipFile(app.ROOT / 'site/downloads' / f'cookbook-by-pengusto-{variant}-{host}.zip') as archive, tempfile.TemporaryDirectory() as temporary:
                        archive.extractall(temporary)
                        root = Path(temporary) / config['name']
                        self.assertEqual(json.loads((root / market_path).read_text()), market)
                        source = market['plugins'][0]['source']
                        plugin = root / (source['path'] if host == 'codex' else source)
                        self.assertEqual({str(p.relative_to(plugin)): p.read_bytes() for p in plugin.rglob('*') if p.is_file()}, files)


if __name__ == '__main__':
    unittest.main()

class NewWorkflowInstallationContracts(unittest.TestCase):
    def test_relative_instruction_links_resolve_in_each_runtime_package(self):
        import posixpath
        import re
        for row in app.catalog():
            for variant in app.VARIANTS:
                slug, files = app.rendered_files(row, variant)
                for name, content in files.items():
                    if not name.endswith('.md'):
                        continue
                    text = content.decode()
                    self.assertNotIn('{{', text, (slug, name))
                    for target in re.findall(r'\]\(([^)]+)\)', text):
                        if '://' in target or target.startswith(('mailto:', '#')):
                            continue
                        path = posixpath.normpath(posixpath.join(posixpath.dirname(name), target.split('#', 1)[0]))
                        self.assertIn(path, files, (slug, name, target))

    def test_confirmed_new_workflows_are_selected_and_rendered_in_both_variants(self):
        expected = {
            'here-we-go-again': 'why-did-it-burn',
            'catch-me-up': 'back-to-the-kitchen',
            'finish-my-prompt': 'finish-my-order',
            'which-name-wins': 'name-that-dish',
            'you-got-this': 'youre-the-chef',
            'explain-the-cookbook': 'show-me-the-kitchen',
            'why-is-it-broken': 'find-the-bad-ingredient',
            'review-my-changes': 'taste-before-serving',
            'can-we-simplify': 'trim-the-recipe',
            'find-our-work': 'find-the-recipe',
        }
        rows = {r['id']: r for r in app.catalog()}
        for variant in app.VARIANTS:
            config, files = app.plugin_files('codex', variant)
            for source_id, kitchen_id in expected.items():
                with self.subTest(variant=variant, source=source_id):
                    self.assertIn(source_id, config['skills'])
                    self.assertEqual(rows[source_id]['install_ids'], {'plain': source_id, 'kitchen': kitchen_id})
                    slug = rows[source_id]['install_ids'][variant]
                    guide = files[f'skills/{slug}/SKILL.md'].decode()
                    metadata = files[f'skills/{slug}/agents/openai.yaml'].decode()
                    self.assertIn(f'name: {slug}\n', guide)
                    self.assertIn(f'${slug}', metadata)
                    self.assertNotIn('{{', guide)
                    self.assertNotIn('/Users/', guide)
                    self.assertNotIn('Enis Uysal', guide)
                    self.assertNotIn(f'skills/{rows[source_id]["install_ids"]["plain" if variant == "kitchen" else "kitchen"]}/SKILL.md', files)

class AutonomousWorkflowContracts(unittest.TestCase):
    def test_modes_and_examples_are_portable_in_each_installed_variant(self):
        row = next(r for r in app.catalog() if r['id'] == 'you-got-this')
        for variant in app.VARIANTS:
            slug, files = app.rendered_files(row, variant)
            other = row['install_ids']['kitchen' if variant == 'plain' else 'plain']
            guide, examples = files['SKILL.md'].decode(), files['examples.md'].decode()
            for text in (guide, examples):
                self.assertIn('$'+slug+' gauntlet', text)
                self.assertIn('$'+slug+' audit', text)
                self.assertIn('$'+slug+' usertest', text)
                self.assertNotIn('$'+other, text)
                self.assertNotIn('{{', text)
            self.assertEqual(files['LICENSE'], (app.ROOT / 'skills/you-got-this/LICENSE').read_bytes())
            self.assertIn('Copyright (c) 2026 Enis Uysal', files['LICENSE'].decode())


class RemoteMarketplaceContracts(unittest.TestCase):
    def test_remote_branches_have_the_native_root_and_exact_skill_package(self):
        import sys
        sys.path.insert(0, str(app.ROOT / 'scripts'))
        import publish_marketplaces
        for variant in app.VARIANTS:
            config, expected = app.plugin_files('codex', variant)
            files = publish_marketplaces.marketplace_files(variant)
            metadata = json.loads(files['.agents/plugins/marketplace.json'])
            self.assertEqual(metadata['plugins'][0]['source']['path'], './plugins/cookbook-by-pengusto')
            self.assertEqual({n.removeprefix('plugins/cookbook-by-pengusto/'): v for n,v in files.items() if n.startswith('plugins/')}, expected)
            self.assertIn(f'--ref {variant}', files['README.md'].decode())
            self.assertNotIn('.mcp.json', files)
