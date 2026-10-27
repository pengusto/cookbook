#!/usr/bin/env python3
"""Local-only development server for Cookbook's stateless Streamable HTTP MCP.

Serves only generated, reviewed Cookbook data. No filesystem browsing, outbound
requests, workflow execution, accounts or durable user state.
"""
import argparse
from functools import partial
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
import unicodedata

PROTOCOLS = ('2025-03-26', '2025-06-18', '2025-11-25')
URI = 'ui://cookbook/remote-v1.html'
MIME = 'text/html;profile=mcp-app'
MAX_BODY = 16384
STOP_WORDS = set('a an and the i my to for of in with how can do want is this it '
                 'ich mein meine ein eine einen und oder das die der zu zur zum '
                 'mit fur wie kann ich mochte bitte projekt project'.split())
# Small bilingual concept groups, not an additional workflow catalog.
CONCEPTS = (
    ('release', 'publish', 'launch', 'veroffentlich', 'teilen', 'sharing'),
    ('bug', 'debug', 'broken', 'fehler', 'kaputt', 'diagnos'),
    ('privacy', 'secret', 'leak', 'geheim', 'sensitive', 'sicherheit'),
    ('legal', 'recht', 'compliance', 'licens', 'lizenz'),
    ('simplif', 'complex', 'vereinfach', 'komplex', 'duplication'),
    ('recap', 'ursprung', 'original', 'goal', 'ziel'),
    ('pause', 'break', 'return', 'wiedereinstieg'),
    ('changelog', 'release notes', 'anderungsnotiz'),
    ('handoff', 'ubergabe', 'abschliess', 'abschluss', 'finish'),
)


def tokens(text):
    folded = unicodedata.normalize('NFKD', text.casefold().replace('ß', 'ss'))
    return re.findall(r'[a-z0-9]+', ''.join(c for c in folded if not unicodedata.combining(c)))


def schema(properties, required=()):
    return {'type': 'object', 'properties': properties, 'required': list(required), 'additionalProperties': False}


class Cookbook:
    def __init__(self, root):
        self.root = Path(root)
        self.data = json.loads((self.root / 'data/workflows.json').read_text())
        self.rows = self.data['workflows']
        self.by_id = {row['id']: row for row in self.rows}
        self.html = (self.root / 'ui/index.html').read_text()
        self.chapters = list(dict.fromkeys(row['chapter'] for row in self.rows))

    def tools(self):
        language = {'type': 'string', 'enum': ['en', 'de'], 'default': 'en'}
        identifier = {'type': 'string', 'enum': list(self.by_id)}
        definitions = [
            ('search_workflows', 'Find Cookbook workflows',
             'Find workflows for a task in English or German. Empty query browses the catalog. '
             'Returns lexical matches, not a guarantee of suitability. Use get_workflow for the full instructions.',
             schema({'query': {'type': 'string', 'maxLength': 500},
                     'chapter': {'type': 'string', 'enum': self.chapters},
                     'limit': {'type': 'integer', 'minimum': 1, 'maximum': 18, 'default': 5}, 'language': language})),
            ('get_workflow', 'Read a Cookbook workflow',
             'Read the full versioned workflow and bundled reference files. Does not execute or install it. '
             'Execution requires the host tools and user authorization described in the instructions.',
             schema({'id': identifier, 'language': language}, ('id',))),
            ('open_cookbook', 'Open Cookbook',
             'Open the interactive recipe book, optionally with IDs returned by search_workflows '
             'and a selected workflow. Reads only Cookbook content; does not start a workflow.',
             schema({'workflow_ids': {'type': 'array', 'items': identifier, 'maxItems': 18, 'uniqueItems': True},
                     'selected_id': identifier, 'language': language})),
        ]
        tools = []
        for name, title, description, input_schema in definitions:
            tool = {'name': name, 'title': title, 'description': description, 'inputSchema': input_schema,
                    'annotations': {'readOnlyHint': True, 'destructiveHint': False, 'openWorldHint': False}}
            if name == 'open_cookbook':
                tool['_meta'] = {'ui': {'resourceUri': URI, 'visibility': ['model', 'app']}}
            tools.append(tool)
        return tools

    def validate(self, name, args):
        definition = next((t for t in self.tools() if t['name'] == name), None)
        if definition is None:
            raise ValueError('Unknown tool')
        spec = definition['inputSchema']
        if not isinstance(args, dict) or set(args) - set(spec['properties']) or set(spec['required']) - set(args):
            raise ValueError('Invalid tool arguments')
        for key, value in args.items():
            rule = spec['properties'][key]
            kind = rule['type']
            if kind == 'string' and (not isinstance(value, str) or len(value) > rule.get('maxLength', 500)):
                raise ValueError('Invalid string argument')
            if kind == 'integer' and (type(value) is not int or not rule['minimum'] <= value <= rule['maximum']):
                raise ValueError('Invalid result limit')
            if 'enum' in rule and value not in rule['enum']:
                raise ValueError('Unknown workflow, chapter or language')
            if kind == 'array' and (not isinstance(value, list) or len(value) > rule['maxItems']
                                    or any(not isinstance(v, str) or v not in self.by_id for v in value)
                                    or len(set(value)) != len(value)):
                raise ValueError('Invalid workflow selection')

    def summary(self, row, language):
        return {key: row[key] for key in ('id', 'title', 'chapter', 'url')} | row['localized'][language]

    def search(self, args):
        terms = set(tokens(args.get('query', ''))) - STOP_WORDS
        groups = [group for group in CONCEPTS if any(any(term.startswith(word) for word in group) for term in terms)]
        ranked = []
        for index, row in enumerate(self.rows):
            if args.get('chapter') and row['chapter'] != args['chapter']:
                continue
            title = tokens(row['title'] + ' ' + row['id'] + ' ' + row['searchTitle'])
            description = tokens(' '.join(v['summary'] + ' ' + v['when'] for v in row['localized'].values()))
            score = sum(5 if any(w.startswith(t) for w in title) else
                        2 if any(w.startswith(t) for w in description) else 0 for t in terms)
            score += sum(8 if any(any(w.startswith(g) for g in group) for w in title) else
                         2 if any(any(w.startswith(g) for g in group) for w in description) else 0 for group in groups)
            if not terms or score:
                ranked.append((-score, index, row))
        ranked.sort(key=lambda item: item[:2])
        language = args.get('language', 'en')
        return {'version': self.data['version'], 'language': language,
                'total': len(ranked), 'workflows': [self.summary(r, language) for _, _, r in ranked[:args.get('limit', 5)]]}

    def call(self, name, args):
        self.validate(name, args)
        language = args.get('language', 'en')
        if name == 'search_workflows':
            result = self.search(args)
        elif name == 'get_workflow':
            row = self.by_id[args['id']]
            result = {'version': self.data['version'], 'language': language,
                      'workflow': self.summary(row, language) | {key: row[key] for key in ('instructions', 'files', 'sha256')},
                      'execution': 'Instructions only. Local tools and separate user authorization are required for execution. '
                                   'Supporting files are returned as text; relative file paths require materializing them first. '
                                   'A $skill invocation works only if that skill is installed. Workflow instructions are in their source language.'}
        else:
            ids = args.get('workflow_ids', list(self.by_id))
            selected = args.get('selected_id', ids[0] if ids else None)
            if selected is not None and selected not in ids:
                raise ValueError('Selected workflow must be included in workflow_ids')
            result = {'version': self.data['version'], 'language': language, 'workflowIds': ids, 'selectedId': selected,
                      'workflows': [self.summary(self.by_id[i], language) for i in ids]}
        return {'structuredContent': result, 'content': [{'type': 'text', 'text': json.dumps(result, ensure_ascii=False)}]}

    def dispatch(self, method, params):
        if method == 'initialize':
            if not isinstance(params.get('protocolVersion'), str) or not isinstance(params.get('capabilities'), dict) or not isinstance(params.get('clientInfo'), dict):
                raise ValueError('Invalid initialization parameters')
            return {'protocolVersion': params['protocolVersion'] if params['protocolVersion'] in PROTOCOLS else PROTOCOLS[-1],
                    'capabilities': {'tools': {}, 'resources': {}},
                    'serverInfo': {'name': 'cookbook-remote', 'version': self.data['version']},
                    'instructions': 'Cookbook provides workflow instructions, not execution. Find relevant workflows, '
                                    'read their prerequisites and limits, and use host tools only within the user request.'}
        if method == 'ping':
            return {}
        if method == 'tools/list':
            return {'tools': self.tools()}
        if method == 'tools/call':
            if set(params) - {'name', 'arguments', '_meta'}:
                raise ValueError('Invalid tool call')
            try:
                return self.call(params.get('name'), params.get('arguments', {}))
            except ValueError as error:
                return {'isError': True, 'content': [{'type': 'text', 'text': str(error)}]}
        resource = {'uri': URI, 'name': 'cookbook', 'mimeType': MIME, 'title': 'Cookbook by Pengusto'}
        if method == 'resources/list':
            return {'resources': [resource]}
        if method == 'resources/templates/list':
            return {'resourceTemplates': []}
        if method == 'resources/read':
            if params.get('uri') != URI:
                raise ValueError('Unknown resource')
            return {'contents': [{**resource, 'text': self.html,
                                  '_meta': {'ui': {'csp': {'connectDomains': [], 'resourceDomains': []}}}}]}
        raise LookupError('Method not found')


class Handler(BaseHTTPRequestHandler):
    server_version = 'CookbookLocal/1'
    html_csp = "default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src data:; font-src data:; connect-src 'self'; frame-ancestors 'self'"

    def __init__(self, *args, cookbook, **kwargs):
        self.cookbook = cookbook
        super().__init__(*args, **kwargs)

    def setup(self):
        super().setup()
        self.connection.settimeout(10)

    def log_message(self, format, *args):
        # The default logger includes request targets. Do not log user input.
        pass

    def respond(self, status, value=None, mime='application/json', allow=False):
        body = b'' if value is None else value.encode() if isinstance(value, str) else json.dumps(value, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header('Content-Type', mime + '; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        if allow:
            self.send_header('Allow', 'POST')
        if mime == 'text/html':
            self.send_header('Content-Security-Policy', self.html_csp)
        self.end_headers()
        self.wfile.write(body)

    def safe_request(self):
        expected = f'127.0.0.1:{self.server.server_port}'
        hosts = {expected, f'localhost:{self.server.server_port}'}
        if self.headers.get('Host') not in hosts or (self.headers.get('Origin') is not None
                and self.headers['Origin'] not in {'http://' + host for host in hosts}):
            self.respond(403, {'error': 'Origin or Host not allowed'})
            return False
        if self.headers.get('MCP-Protocol-Version', PROTOCOLS[0]) not in PROTOCOLS:
            self.respond(400, {'error': 'Unsupported MCP protocol version'})
            return False
        return True

    def do_GET(self):
        if not self.safe_request():
            return
        if self.path == '/preview':
            self.respond(200, self.cookbook.html, 'text/html')
        elif self.path == '/mcp':
            self.respond(405, allow=True)
        else:
            self.respond(404)

    def do_DELETE(self):
        if self.safe_request():
            self.respond(405 if self.path == '/mcp' else 404, allow=self.path == '/mcp')

    def do_POST(self):
        if not self.safe_request():
            return
        if self.path != '/mcp':
            self.respond(404)
            return
        if self.headers.get_content_type() != 'application/json':
            self.respond(415, {'error': 'Expected application/json'})
            return
        accept = self.headers.get('Accept', '')
        if not all(mime in accept for mime in ('application/json', 'text/event-stream')):
            self.respond(406, {'error': 'Accept must include application/json and text/event-stream'})
            return
        try:
            size = int(self.headers.get('Content-Length', '-1'))
        except ValueError:
            size = -1
        if self.headers.get('Transfer-Encoding') or not 0 <= size <= MAX_BODY:
            self.respond(413 if size > MAX_BODY else 400, {'error': 'Invalid request length'})
            return
        try:
            request = json.loads(self.rfile.read(size).decode('utf-8'))
        except (ValueError, UnicodeError):
            self.respond(400, {'jsonrpc': '2.0', 'id': None, 'error': {'code': -32700, 'message': 'Parse error'}})
            return
        if (not isinstance(request, dict) or request.get('jsonrpc') != '2.0'
                or not isinstance(request.get('method'), str)
                or ('id' in request and (type(request['id']) not in (str, int)))
                or not isinstance(request.get('params', {}), dict)):
            self.respond(400, {'jsonrpc': '2.0', 'id': None, 'error': {'code': -32600, 'message': 'Invalid request'}})
            return
        if 'id' not in request:
            self.respond(202)
            return
        reply = {'jsonrpc': '2.0', 'id': request['id']}
        try:
            reply['result'] = self.cookbook.dispatch(request['method'], request.get('params', {}))
        except (ValueError, LookupError) as error:
            reply['error'] = {'code': -32602 if isinstance(error, ValueError) else -32601, 'message': str(error)}
        self.respond(200, reply)


def create_server(root, port=8767):
    cookbook = Cookbook(root)
    return ThreadingHTTPServer(('127.0.0.1', port), partial(Handler, cookbook=cookbook))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8767)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    with create_server(root, args.port) as server:
        print(f'Local MCP: http://127.0.0.1:{server.server_port}/mcp', flush=True)
        print(f'Local book preview: http://127.0.0.1:{server.server_port}/preview', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()
