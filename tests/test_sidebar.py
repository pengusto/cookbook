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
