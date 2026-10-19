#!/usr/bin/env python3
"""Read-only, dependency-free stdio MCP server for the local Cookbook sidebar."""
import base64
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URI = 'ui://cookbook/catalog-v1'
MIME = 'text/html;profile=mcp-app'
VERSION = '0.3.0'


def icons():
    return [{'src': 'data:image/svg+xml;base64,' + base64.b64encode(
        (ROOT / 'assets/sidebar-icon.svg').read_bytes()).decode(),
        'mimeType': 'image/svg+xml', 'sizes': ['any']}]


def tool():
    return {'name': 'open_cookbook', 'title': 'Cookbook by Pengusto',
            'description': 'Open the local Cookbook skill catalog. Read-only; no installation or publishing.',
            'icons': icons(), 'inputSchema': {'type': 'object', 'properties': {}, 'additionalProperties': False},
            'annotations': {'readOnlyHint': True, 'destructiveHint': False, 'openWorldHint': False},
            '_meta': {'ui': {'resourceUri': URI, 'visibility': ['app']},
                      'openai/ui': {'entrypoints': [{'type': 'global'}]}}}


def resource():
    return {'uri': URI, 'name': 'cookbook', 'title': 'Cookbook by Pengusto', 'mimeType': MIME}


def dispatch(method, params):
    if method == 'initialize':
        requested = params.get('protocolVersion')
        version = requested if requested in ('2024-11-05', '2025-03-26', '2025-06-18', '2025-11-25') else '2025-11-25'
        return {'protocolVersion': version, 'capabilities': {'tools': {}, 'resources': {}},
                'serverInfo': {'name': 'cookbook-sidebar', 'version': VERSION, 'icons': icons()}}
    if method == 'ping':
        return {}
    if method == 'tools/list':
        return {'tools': [tool()]}
    if method == 'tools/call':
        if params.get('name') != 'open_cookbook' or params.get('arguments', {}) != {}:
            raise ValueError('Unknown tool or unsupported arguments')
        return {'content': [{'type': 'text', 'text': 'Local Cookbook catalog opened.'}]}
    if method == 'resources/list':
        return {'resources': [resource()]}
    if method == 'resources/templates/list':
        return {'resourceTemplates': []}
    if method == 'resources/read':
        if params.get('uri') != URI:
            raise ValueError('Unknown resource')
        return {'contents': [{**resource(), 'text': (ROOT / 'ui/index.html').read_text(),
                             '_meta': {'ui': {'csp': {'connectDomains': [], 'resourceDomains': []}},
                                       'openai/ui': {'preferredDisplayMode': 'fullscreen',
                                                     'availableDisplayModes': ['fullscreen']}}}]}
    raise LookupError('Method not found')


def main():
    for line in sys.stdin:
        try:
            request = json.loads(line)
        except ValueError:
            print(json.dumps({'jsonrpc': '2.0', 'id': None, 'error': {'code': -32700, 'message': 'Parse error'}}), flush=True)
            continue
        if not isinstance(request, dict) or request.get('jsonrpc') != '2.0' or not isinstance(request.get('method'), str):
            reply = {'error': {'code': -32600, 'message': 'Invalid request'}}
        elif 'id' not in request:
            continue
        else:
            try:
                params = request.get('params', {})
                if not isinstance(params, dict):
                    raise ValueError('Parameters must be an object')
                reply = {'result': dispatch(request['method'], params)}
            except ValueError as error:
                reply = {'error': {'code': -32602, 'message': str(error)}}
            except LookupError:
                reply = {'error': {'code': -32601, 'message': 'Method not found'}}
            except OSError:
                reply = {'error': {'code': -32603, 'message': 'Local app resource unavailable'}}
        request_id = request.get('id') if isinstance(request, dict) else None
        print(json.dumps({'jsonrpc': '2.0', 'id': request_id, **reply}), flush=True)


if __name__ == '__main__':
    main()
