import base64
import xml.etree.ElementTree as ET
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest
import zipfile

spec = importlib.util.spec_from_file_location('sidebar_builder', Path(__file__).resolve().parents[1] / 'scripts/cookbook.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class SidebarContracts(unittest.TestCase):
    def test_book_has_twelve_complete_locales_and_both_names_with_installed_invocation(self):
        import re
        for variant in ('plain', 'kitchen'):
            files = builder.sidebar_files(variant)
            text = files['ui/index.html'].decode()
            payload = re.search(r'<script id="cookbook-data" type="application/json">(.*?)</script>', text, re.S)
            data = json.loads(payload[1])
            self.assertEqual(set(data['locales']), {'de','en','fr','es','pt-BR','it','tr','ja','ko','zh-CN','ar','hi'})
            self.assertEqual([r['id'] for r in data['recipes']], [r['install_ids'][variant] for r in builder.catalog()])
            self.assertEqual(data['version'], '0.5.1')
            self.assertEqual(data['variant'], variant)
            self.assertEqual([r['names'] for r in data['recipes']], [{'plain': r['title'], 'kitchen': r['cooking_title']} for r in builder.catalog()])
            self.assertIn("$('invocation').textContent='$'+recipe.id", text)
            self.assertIn('cookbook-naming', text)
            self.assertIn("let appearance='system'", text)
            for locale in data['locales'].values():
                self.assertEqual(len(locale['stepNotes12']), 4)
                self.assertEqual(len(locale['verifications']), len(builder.catalog()))
                self.assertEqual(len(locale['ingredientLists']), len(builder.catalog()))
                self.assertEqual(len(locale['intros'].split('|')), len(builder.catalog()))
                self.assertTrue(all(len(locale['steps'+str(i)].split('|')) == 4 for i in range(len(builder.catalog()))))
            self.assertIn('prefers-reduced-motion', text)
            self.assertIn('navigator.clipboard.writeText', text)
            self.assertIn('page-turn-leaf', text)
            self.assertIn('data:image/webp;base64,', text)
            self.assertIn('data:font/woff2;base64,', text)
            self.assertLess(len(files['ui/index.html']), 3 * 1024 * 1024)
            self.assertIn('licenses/animejs.txt', files)
            self.assertIn('licenses/caveat.txt', files)

    def test_inline_data_cannot_terminate_script_and_no_runtime_remote_assets(self):
        from unittest.mock import patch
        import re
        original = Path.read_text
        def read(path, *args, **kwargs):
            text = original(path, *args, **kwargs)
            if path == builder.ROOT / 'ui/locales.json':
                data = json.loads(text)
                data['de']['motto'] = '</script><script>unexpected()</script>'
                return json.dumps(data)
            return text
        with patch.object(Path, 'read_text', read):
            text = builder.sidebar_files('kitchen')['ui/index.html'].decode()
        self.assertNotIn('</script><script>unexpected()', text)
        self.assertFalse(re.search(r'<(?:script|link|img)[^>]+(?:src|href)=["\']https?://', text))
        self.assertFalse(re.search(r'url\(["\']?https?://', text))

    def test_stdio_entrypoint_icons_resource_and_rejections(self):
        root = builder.ROOT / 'dist/plain/sidebar/plugins/cookbook-sidebar'
        requests = [
            {'id': 1, 'method': 'initialize', 'params': {'protocolVersion': '2025-11-25'}},
            {'method': 'notifications/initialized'},
            {'id': 2, 'method': 'tools/list'},
            {'id': 3, 'method': 'tools/call', 'params': {'name': 'open_cookbook', 'arguments': {}}},
            {'id': 4, 'method': 'resources/read', 'params': {'uri': 'ui://cookbook/catalog-v1'}},
            {'id': 5, 'method': 'resources/read', 'params': {'uri': 'file:///etc/passwd'}},
            {'id': 6, 'method': 'tools/call', 'params': {'name': 'open_cookbook', 'arguments': {'install': True}}},
            {'id': 7, 'method': 'not/a/method'},
        ]
        payload = '\n'.join(json.dumps({'jsonrpc': '2.0', **r}) for r in requests) + '\n'
        result = subprocess.run([sys.executable, str(root / 'scripts/sidebar_server.py')],
                                input=payload, capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        replies = {r['id']: r for r in map(json.loads, result.stdout.splitlines())}
        self.assertEqual(len(replies), 7)  # Notifications must not receive replies.
        self.assertEqual(replies[1]['result']['protocolVersion'], '2025-11-25')
        tool = replies[2]['result']['tools'][0]
        self.assertEqual(tool['_meta']['openai/ui']['entrypoints'], [{'type': 'global'}])
        self.assertEqual(len(tool['icons']), 1)
        icon = tool['icons'][0]
        self.assertEqual(icon['mimeType'], 'image/svg+xml')
        self.assertTrue(icon['src'].startswith('data:image/svg+xml;base64,'))
        svg = base64.b64decode(icon['src'].split(',', 1)[1])
        self.assertEqual(svg, (builder.ROOT / 'assets/sidebar-icon.svg').read_bytes())
        tree = ET.fromstring(svg)
        self.assertEqual(tree.attrib['viewBox'], '0 0 20 20')
        self.assertTrue(any(e.get('fill-rule') == 'evenodd' for e in tree.iter()))
        for element in tree.iter():
            self.assertNotIn('opacity', element.attrib)
            for attribute in ('fill', 'stroke'):
                if attribute in element.attrib:
                    self.assertIn(element.attrib[attribute], ('none', 'currentColor'))
        self.assertIn('result', replies[3])
        resource = replies[4]['result']['contents'][0]
        self.assertEqual(resource['mimeType'], 'text/html;profile=mcp-app')
        self.assertIn('ui/initialize', resource['text'])
        self.assertEqual(resource['_meta']['ui']['csp']['connectDomains'], [])
        for row in builder.catalog():
            self.assertIn(row['title'], resource['text'])
        self.assertEqual(replies[5]['error']['code'], -32602)
        self.assertEqual(replies[6]['error']['code'], -32602)
        self.assertEqual(replies[7]['error']['code'], -32601)

    def test_companion_archive_has_no_duplicate_skills(self):
        expected = builder.sidebar_files()
        self.assertFalse(any(name.startswith('skills/') for name in expected))
        with zipfile.ZipFile(builder.ROOT / 'dist/plain/sidebar/cookbook-sidebar.zip') as archive:
            self.assertEqual(set(archive.namelist()), {f'cookbook-sidebar/{n}' for n in expected})
            for name, data in expected.items():
                self.assertEqual(archive.read(f'cookbook-sidebar/{name}'), data)
                self.assertEqual((builder.ROOT / 'dist/plain/sidebar/plugins/cookbook-sidebar' / name).read_bytes(), data)

class RecipeIconContracts(unittest.TestCase):
    def test_utensils_follow_stable_ids_in_both_variants_and_landing(self):
        import re
        icons = builder.recipe_icons()
        self.assertEqual(len(set(icon['id'] for icon in icons.values())), len(builder.catalog()))
        for variant in ('plain', 'kitchen'):
            page = builder.sidebar_files(variant)['ui/index.html'].decode()
            data = json.loads(re.search(r'<script id="cookbook-data" type="application/json">(.*?)</script>', page, re.S)[1])
            expected = {row['install_ids'][variant]: icons[row['id']]['id'] for row in builder.catalog()}
            self.assertEqual({row['id']: row['icon'] for row in data['recipes']}, expected)
            for icon in icons.values():
                self.assertEqual(page.count('id="recipe-' + icon['id'] + '"'), 1)
                self.assertIn(icon['body'], builder.render_landing(builder.catalog(), 'en', variant))
            self.assertIn("icon('recipe-'+recipe.icon)", page)
            self.assertIn("$('recipe-emblem').setAttribute('href','#recipe-'+recipe.icon)", page)

    def test_icon_source_rejects_active_svg_content(self):
        from unittest.mock import patch
        original = Path.read_text
        def injected(path, *args, **kwargs):
            text = original(path, *args, **kwargs)
            if path == builder.ROOT / 'ui/recipe-icons.json':
                data = json.loads(text)
                data['start-it-right']['body'] = '<path onload="unexpected()" d="M1 1"/>'
                return json.dumps(data)
            return text
        with patch.object(Path, 'read_text', injected):
            with self.assertRaises(ValueError):
                builder.recipe_icons()
