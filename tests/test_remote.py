"""Real loopback transport and canonical-content contracts for the remote runtime."""
import hashlib
import http.client
import importlib.util
import json
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


builder = module('remote_builder', ROOT / 'scripts/cookbook.py')
remote = module('remote_runtime', ROOT / 'scripts/remote_server.py')


class RemoteContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory(prefix='cookbook-remote-test-')
        cls.addClassCleanup(cls.temporary.cleanup)
        cls.root = Path(cls.temporary.name)
        for variant in builder.VARIANTS:
            for name, data in builder.remote_files(variant).items():
                path = cls.root / variant / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
        cls.app = remote.Cookbook(cls.root / 'kitchen')
        cls.server = remote.create_server(cls.root / 'kitchen', 0)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.addClassCleanup(cls.close_server)

    @classmethod
    def close_server(cls):
        cls.server.shutdown()
        cls.thread.join(timeout=5)
        cls.server.server_close()

    def request(self, method='POST', path='/mcp', message=None, headers=None, raw=None):
        connection = http.client.HTTPConnection('127.0.0.1', self.server.server_port, timeout=5)
        self.addCleanup(connection.close)
        defaults = {'Content-Type': 'application/json', 'Accept': 'application/json, text/event-stream',
                    'MCP-Protocol-Version': remote.PROTOCOLS[-1]}
        defaults.update(headers or {})
        body = raw if raw is not None else json.dumps(message) if message is not None else None
        connection.request(method, path, body=body, headers=defaults)
        response = connection.getresponse()
        result = response.read()
        return response.status, dict(response.getheaders()), result

    def rpc(self, method, params=None):
        status, headers, body = self.request(message={'jsonrpc': '2.0', 'id': 7, 'method': method, 'params': params or {}})
        self.assertEqual(status, 200)
        self.assertIn('application/json', headers['Content-Type'])
        reply = json.loads(body)
        self.assertEqual(reply['id'], 7)
        return reply

    def test_http_client_lifecycle_tools_and_read_only_ui(self):
        result = self.rpc('initialize', {'protocolVersion': '2025-11-25', 'capabilities': {},
                                         'clientInfo': {'name': 'contract-test', 'version': '1'}})['result']
        self.assertEqual(result['protocolVersion'], '2025-11-25')
        self.assertEqual(set(result['capabilities']), {'tools', 'resources'})
        self.assertEqual(self.request(message={'jsonrpc': '2.0', 'method': 'notifications/initialized'})[::2], (202, b''))
        tools = self.rpc('tools/list')['result']['tools']
        self.assertEqual([t['name'] for t in tools], ['search_workflows', 'get_workflow', 'open_cookbook'])
        self.assertTrue(all(t['annotations'] == {'readOnlyHint': True, 'destructiveHint': False, 'openWorldHint': False} for t in tools))
        self.assertNotIn('_meta', tools[0])
        self.assertNotIn('_meta', tools[1])
        self.assertEqual(tools[2]['_meta']['ui']['resourceUri'], remote.URI)
        found = self.rpc('tools/call', {'name': 'search_workflows', 'arguments': {'query': 'debug bug'}})['result']['structuredContent']
        chosen = found['workflows'][0]['id']
        self.assertEqual(chosen, 'find-the-bad-ingredient')
        opened = self.rpc('tools/call', {'name': 'open_cookbook', 'arguments': {'workflow_ids': [chosen], 'selected_id': chosen}})['result']['structuredContent']
        self.assertEqual(opened['selectedId'], chosen)
        resource = self.rpc('resources/read', {'uri': remote.URI})['result']['contents'][0]
        self.assertEqual(resource['mimeType'], remote.MIME)
        self.assertIn('remote-query', resource['text'])
        self.assertIn('ui/notifications/tool-result', resource['text'])
        self.assertEqual(resource['_meta']['ui']['csp']['connectDomains'], [])
        self.assertEqual(self.rpc('ping')['result'], {})

    def test_queries_bilingual_filters_empty_and_unknown(self):
        for query in ('debug bug', 'kaputt Fehler', 'aktuellen Fehler beheben'):
            with self.subTest(query=query):
                found = self.app.call('search_workflows', {'query': query})['structuredContent']
                self.assertEqual(found['workflows'][0]['id'], 'find-the-bad-ingredient')
        for query in ('publish release', 'veröffentlichen'):
            found = self.app.call('search_workflows', {'query': query, 'chapter': 'release'})['structuredContent']
            self.assertIn('ready-to-serve', [r['id'] for r in found['workflows']])
        found = self.app.call('search_workflows', {'query': '', 'limit': 18, 'language': 'de'})['structuredContent']
        self.assertEqual(len(found['workflows']), 18)
        self.assertEqual(found['total'], 18)
        self.assertEqual(found['workflows'][0]['summary'], self.app.rows[0]['localized']['de']['summary'])
        self.assertEqual(self.app.call('search_workflows', {'query': 'xyzzqfuzz'})['structuredContent']['workflows'], [])
        filtered = self.app.call('search_workflows', {'chapter': 'closing'})['structuredContent']['workflows']
        self.assertTrue(filtered)
        self.assertTrue(all(r['chapter'] == 'closing' for r in filtered))

    def test_exact_rendered_instructions_references_hashes_and_single_variant(self):
        for variant in builder.VARIANTS:
            app = remote.Cookbook(self.root / variant)
            for source in builder.catalog():
                slug, rendered = builder.rendered_files(source, variant)
                result = app.call('get_workflow', {'id': slug})['structuredContent']
                workflow = result['workflow']
                self.assertEqual(workflow['instructions'].encode(), rendered['SKILL.md'])
                self.assertEqual(workflow['sha256'], hashlib.sha256(rendered['SKILL.md']).hexdigest())
                self.assertEqual({name: value['text'].encode() for name, value in workflow['files'].items()},
                                 {name: data for name, data in rendered.items() if name != 'SKILL.md'})
                self.assertTrue(all(hashlib.sha256(v['text'].encode()).hexdigest() == v['sha256'] for v in workflow['files'].values()))
                self.assertNotIn('{{', workflow['instructions'])
                self.assertIn('Local tools', result['execution'])
            other = 'let-them-see-it' if variant == 'kitchen' else 'ready-to-serve'
            with self.assertRaises(ValueError):
                app.call('get_workflow', {'id': other})

    def test_unknown_ids_paths_arguments_and_resource_rejected(self):
        invalid = [('get_workflow', {'id': '../../.git/config'}),
                   ('get_workflow', {}), ('get_workflow', {'id': 'ready-to-serve', 'language': 'xx'}),
                   ('search_workflows', {'limit': True}), ('search_workflows', {'limit': 0}),
                   ('search_workflows', {'query': 'x' * 501}), ('search_workflows', {'query': []}),
                   ('search_workflows', {'chapter': 'unknown'}), ('search_workflows', {'execute': True}),
                   ('open_cookbook', {'workflow_ids': ['ready-to-serve'] * 2}),
                   ('open_cookbook', {'workflow_ids': [{}]}),
                   ('open_cookbook', {'workflow_ids': [], 'selected_id': 'ready-to-serve'}),
                   ('open_cookbook', {'workflow_ids': [] , 'execute': True}), ('unknown', {})]
        for name, arguments in invalid:
            with self.subTest(name=name, arguments=arguments):
                result = self.rpc('tools/call', {'name': name, 'arguments': arguments})['result']
                self.assertTrue(result['isError'])
                self.assertNotIn('structuredContent', result)
        self.assertEqual(self.rpc('resources/read', {'uri': 'file:///etc/passwd'})['error']['code'], -32602)
        self.assertEqual(self.rpc('run_command')['error']['code'], -32601)

    def test_http_origin_host_protocol_media_and_body_validation(self):
        for method in ('GET', 'POST', 'DELETE'):
            self.assertEqual(self.request(method=method, headers={'Origin': 'https://attacker.invalid'})[0], 403)
            self.assertEqual(self.request(method=method, headers={'Host': 'attacker.invalid'})[0], 403)
        message = {'jsonrpc': '2.0', 'id': 1, 'method': 'ping'}
        self.assertEqual(self.request(message=message, headers={'Origin': f'http://127.0.0.1:{self.server.server_port}'})[0], 200)
        self.assertEqual(self.request(message=message, headers={'MCP-Protocol-Version': 'unknown'})[0], 400)
        self.assertEqual(self.request(message=message, headers={'Content-Type': 'text/plain'})[0], 415)
        self.assertEqual(self.request(message=message, headers={'Accept': 'text/html'})[0], 406)
        self.assertEqual(self.request(raw='x' * (remote.MAX_BODY + 1))[0], 413)
        for raw in ('{', '\ud800', '[]', 'null', '{}', '{"jsonrpc":"2.0","method":"ping","id":true}'):
            if raw == '\ud800':
                raw = b'\xff'
            self.assertEqual(self.request(raw=raw)[0], 400)

    def test_no_file_serving_sessions_or_request_logging(self):
        with patch.object(remote.Handler, 'log_message') as log:
            self.assertEqual(self.request(method='GET', path='/data/workflows.json')[0], 404)
            self.assertEqual(self.request(method='GET', path='/../../.git/config')[0], 404)
            self.assertEqual(self.request(method='GET', path='/mcp')[0], 405)
            self.assertEqual(self.request(method='DELETE')[0], 405)
            status, headers, body = self.request(method='GET', path='/preview')
            self.assertEqual(status, 200)
            self.assertIn(b'remote-query', body)
            self.assertIn("frame-ancestors 'self'", headers['Content-Security-Policy'])
        # BaseHTTPRequestHandler invokes the overridden no-op; it never emits its arguments.
        self.assertTrue(log.called)
        for variant in builder.VARIANTS:
            files = builder.remote_files(variant)
            self.assertNotIn('.mcp.json', files)
            self.assertNotIn('.codex-plugin/plugin.json', files)
            self.assertNotIn('scripts/sidebar_server.py', files)
            local_ui = builder.sidebar_files(variant)['ui/index.html']
            self.assertNotIn(b'remote-query', local_ui)
            self.assertIn(b'cookbook-init', local_ui)


if __name__ == '__main__':
    unittest.main()
