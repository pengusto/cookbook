#!/usr/bin/env python3
"""Build and verify curated skill snapshots; never execute skill instructions."""
import argparse
import hashlib
import html
import http.server
import json
import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPE_FIELDS = ('when', 'ingredients', 'steps', 'verify', 'result')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def catalog():
    rows = json.loads((ROOT / 'catalog.json').read_text())
    ids = set()
    for row in rows:
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', row['id']) or row['id'] in ids:
            raise ValueError('Invalid or duplicate recipe ID')
        ids.add(row['id'])
        if any(not row[field].strip() for field in (*RECIPE_FIELDS, 'title', 'cooking_title')):
            raise ValueError('Incomplete recipe')
        if row['status'] not in ('snapshot', 'candidate'):
            raise ValueError('Unknown status')
    return rows


def package_files(row):
    folder = ROOT / 'skills' / row['id']
    files = row['files']
    if not {'SKILL.md', 'LICENSE'} <= set(files):
        raise ValueError('Missing skill or license')
    for name, expected in files.items():
        relative = Path(name)
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError('Unsafe package path')
        path = folder / relative
        if any(p.is_symlink() for p in [path, *path.parents]) or not path.is_file():
            raise ValueError('Missing file or symlink in package')
        if sha(path.read_bytes()) != expected:
            raise ValueError(f'Hash mismatch: {row["id"]}/{name}')
    actual = {str(p.relative_to(folder)) for p in folder.rglob('*') if p.is_file()}
    if actual != set(files):
        raise ValueError('Unexpected snapshot files')
    text = (folder / 'SKILL.md').read_text()
    if not text.startswith('---\n') or '\n---\n' not in text[4:]:
        raise ValueError('Invalid frontmatter')
    front = text[4:text.index('\n---\n', 4)]
    if not re.search(rf'(?m)^name: {re.escape(row["id"])}$', front):
        raise ValueError('Skill name mismatch')
    if not re.search(r'(?m)^description:\s*\S', front):
        raise ValueError('Missing description')
    return folder, files


def zip_bytes(row, target):
    folder, files = package_files(row)
    write_zip({f'{row["id"]}/{name}': (folder / name).read_bytes() for name in files}, target)


def write_zip(files, target):
    with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_STORED) as archive:
        for name in sorted(files):
            info = zipfile.ZipInfo(name, (2020, 1, 1, 0, 0, 0))
            info.create_system = 3
            mode = 0o755 if '/bin/' in name else 0o644
            info.external_attr = (0o100000 | mode) << 16
            archive.writestr(info, files[name])


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()


def plugin_files(host):
    if host not in ('codex', 'claude'):
        raise ValueError('Unknown plugin host')
    config = json.loads((ROOT / 'bundle.json').read_text())
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', config['name']):
        raise ValueError('Invalid bundle name')
    if not re.fullmatch(r'\d+\.\d+\.\d+', config['version']):
        raise ValueError('Invalid review bundle version')
    selected = config['skills']
    if not selected or len(set(selected)) != len(selected):
        raise ValueError('Empty or duplicate bundle selection')
    rows = {row['id']: row for row in catalog()}
    manifest = {key: config[key] for key in ('name', 'version', 'description', 'author', 'license')}
    manifest['keywords'] = config['keywords']
    # Use the documented compatibility manifest for Codex and native Claude layout.
    if host == 'codex':
        manifest['skills'] = './skills/'
        manifest['requires_local_executor'] = True
        listing = json.loads((ROOT / 'store/listing.json').read_text())
        for key, limit in (('displayName', 30), ('shortDescription', 30),
                           ('longDescription', 4000), ('developerName', 80)):
            if not isinstance(listing.get(key), str) or not 0 < len(listing[key]) <= limit:
                raise ValueError(f'Invalid listing field: {key}')
        if len(listing['capabilities']) > 20 or any(len(s) > 120 for s in listing['capabilities']):
            raise ValueError('Invalid capabilities')
        if len(listing['defaultPrompt']) > 3 or any(len(s) > 128 for s in listing['defaultPrompt']):
            raise ValueError('Invalid starter prompts')
        manifest['interface'] = listing
        translation = json.loads((ROOT / 'store/listing.de.json').read_text())
        if not 0 < len(translation['subtitle']) <= 30 or not 0 < len(translation['description']) <= 4000:
            raise ValueError('Invalid German listing translation')
        manifest['extensions'] = {'com.openai': {'publication': {'translations': {'de-DE': translation}}}}
    else:
        manifest['displayName'] = 'Vibe Coding Cookbook'
        manifest['icon'] = './assets/icon.png'
    files = {f'.{host}-plugin/plugin.json': json_bytes(manifest), 'LICENSE': (ROOT / 'LICENSE').read_bytes()}
    for name in ('icon.svg', 'icon-dark.svg', 'icon.png', 'icon-dark.png'):
        files[f'assets/{name}'] = (ROOT / 'assets' / name).read_bytes()
    if host == 'codex':
        for key in ('logo', 'logoDark', 'composerIcon', 'composerIconDark'):
            path = manifest['interface'][key]
            if not path.startswith('./assets/') or path[2:] not in files:
                raise ValueError(f'Missing listing asset: {key}')
    sources = []
    for slug in selected:
        row = rows.get(slug)
        if not row or row['status'] != 'snapshot':
            raise ValueError(f'Bundle requires a reviewed installable snapshot: {slug}')
        folder, names = package_files(row)
        files.update({f'skills/{slug}/{name}': (folder / name).read_bytes() for name in names})
        sources.append({key: row[key] for key in ('id', 'license', 'repository', 'revision', 'files')})
    files['SOURCES.json'] = json_bytes({'bundle': config['name'], 'version': config['version'], 'skills': sources})
    files['README.md'] = (ROOT / 'templates/plugin-README.md').read_bytes()
    files['README.de.md'] = (ROOT / 'templates/plugin-README.de.md').read_bytes()
    return config, files


def marketplace(host, config):
    name = config['name']
    if host == 'codex':
        return '.agents/plugins/marketplace.json', {
            'name': 'cookbook-local', 'plugins': [{
                'name': name, 'source': {'source': 'local', 'path': f'./plugins/{name}'},
                'policy': {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'},
                'category': 'Developer Tools'}]}
    return '.claude-plugin/marketplace.json', {
        'name': 'cookbook-local', 'owner': config['author'],
        'metadata': {'description': 'Local review marketplace for the selected Cookbook skills.'},
        'plugins': [{'name': name, 'source': f'./plugins/{name}', 'description': config['description']}]}


def build_plugins(downloads):
    sums = []
    for host in ('codex', 'claude'):
        config, files = plugin_files(host)
        root = ROOT / 'dist' / host
        plugin = root / 'plugins' / config['name']
        for name, data in files.items():
            path = plugin / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            path.chmod(0o755 if '/bin/' in name else 0o644)
        name, value = marketplace(host, config)
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(json_bytes(value))
        target = downloads / f'{config["name"]}-{host}.zip'
        write_zip({f'{config["name"]}/{name}': data for name, data in files.items()}, target)
        sums.append(f'{sha(target.read_bytes())}  {target.name}')
    return sums


def sidebar_files():
    """Optional read-only companion; does not duplicate installed skills."""
    name = 'cookbook-sidebar'
    listing = json.loads((ROOT / 'store/listing.json').read_text())
    listing.update(displayName='Cookbook', shortDescription='Browse local skill recipes',
                   longDescription='Read the local Cookbook catalog in the sidebar. Requires Python 3.10+. Does not install skills, edit files, or publish.',
                   capabilities=['Browse the local Cookbook'], defaultPrompt=[])
    manifest = {'name': name, 'version': '0.1.3', 'description': listing['longDescription'],
                'author': {'name': 'Pengusto'}, 'license': 'MIT', 'interface': listing,
                'mcpServers': './.mcp.json'}
    config = {'mcpServers': {name: {'command': 'python3',
              'args': ['./scripts/sidebar_server.py'], 'cwd': './'}}}
    cards = []
    for row in catalog():
        esc = html.escape
        fields = ''.join(f'<dt>{esc(key)}</dt><dd>{esc(row[key])}</dd>'
                         for key in (*RECIPE_FIELDS, 'limits'))
        cards.append(f'<article><p class="eyebrow">{esc(row["phase"])}</p><h2>{esc(row["title"])}</h2><p class="cooking-title">{esc(row["cooking_title"])}</p>'
                     f'<p>{esc(row["summary"])}</p><p class="status">{esc(row["license"])} · {esc(row["status"])}</p>'
                     f'<details><summary>Rezept öffnen</summary><dl>{fields}</dl>'
                     f'<p>Beispielaufruf für einen separat installierten Skill:</p><code>{esc(row["prompt"])}</code></details></article>')
    css = (ROOT / 'templates/index.html').read_text().split('<style>')[1].split('</style>')[0]
    bridge = '''<script>
const initId = 'cookbook-init';
addEventListener('message', event => {
  if (event.source !== parent || !event.data || event.data.jsonrpc !== '2.0') return;
  if (event.data.id === initId && event.data.result) {
    parent.postMessage({jsonrpc:'2.0',method:'ui/notifications/initialized'}, '*');
  }
});
parent.postMessage({jsonrpc:'2.0',id:initId,method:'ui/initialize',params:{protocolVersion:'2026-01-26',appInfo:{name:'cookbook-sidebar',version:'0.1.3'},appCapabilities:{}}}, '*');
</script>'''
    page = '<!doctype html><html lang="de"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    page += f'<title>Cookbook</title><style>{css}</style><header><p class="eyebrow">Lokales Cookbook</p><h1>Vibe Coding Cookbook.</h1>'
    page += '<p>Sieben Rezepte, sieben separat installierbare Skills. Diese Ansicht ist zum Lesen; sie installiert oder veröffentlicht nichts.</p></header>'
    page += '<main><div class="grid">' + ''.join(cards) + '</div></main>' + bridge + '</html>'
    files = {'.codex-plugin/plugin.json': json_bytes(manifest), '.mcp.json': json_bytes(config),
             'scripts/sidebar_server.py': (ROOT / 'scripts/sidebar_server.py').read_bytes(),
             'ui/index.html': page.encode(), 'LICENSE': (ROOT / 'LICENSE').read_bytes()}
    for asset in ('icon.png', 'icon-dark.png', 'icon.svg', 'icon-dark.svg', 'sidebar-icon.svg'):
        files[f'assets/{asset}'] = (ROOT / 'assets' / asset).read_bytes()
    return files


def build_sidebar():
    root = ROOT / 'dist/sidebar'
    files = sidebar_files()
    for name, data in files.items():
        path = root / 'plugins/cookbook-sidebar' / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    market = {'name': 'cookbook-sidebar-local', 'plugins': [{'name': 'cookbook-sidebar',
              'source': {'source': 'local', 'path': './plugins/cookbook-sidebar'},
              'policy': {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'}, 'category': 'Developer Tools'}]}
    path = root / '.agents/plugins/marketplace.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(json_bytes(market))
    write_zip({f'cookbook-sidebar/{name}': data for name, data in files.items()}, root / 'cookbook-sidebar.zip')


def check_plugins():
    for host in ('codex', 'claude'):
        config, files = plugin_files(host)
        root = ROOT / 'dist' / host
        plugin = root / 'plugins' / config['name']
        actual = {str(p.relative_to(plugin)) for p in plugin.rglob('*') if p.is_file()}
        if actual != set(files):
            raise ValueError('Unexpected or missing generated plugin files; review stale build output')
        for name, data in files.items():
            path = plugin / name
            if path.is_symlink() or path.read_bytes() != data:
                raise ValueError(f'Plugin differs from reviewed inputs: {host}/{name}')
        market_path, value = marketplace(host, config)
        if (root / market_path).read_bytes() != json_bytes(value):
            raise ValueError('Marketplace configuration differs')
        with zipfile.ZipFile(ROOT / 'site/downloads' / f'{config["name"]}-{host}.zip') as archive:
            expected = {f'{config["name"]}/{name}': data for name, data in files.items()}
            if set(archive.namelist()) != set(expected) or archive.testzip():
                raise ValueError('Plugin archive file list differs')
            if any(archive.read(name) != data for name, data in expected.items()):
                raise ValueError('Plugin archive bytes differ')


def schema_script(rows):
    """Describe only the visible collection; omit unconfirmed public identifiers."""
    data = {
        '@context': 'https://schema.org', '@type': 'CollectionPage',
        'name': 'Vibe Coding Cookbook', 'inLanguage': 'de',
        'mainEntity': {
            '@type': 'ItemList', 'numberOfItems': len(rows),
            'itemListElement': [
                {'@type': 'ListItem', 'position': index,
                 'item': {'@type': 'CreativeWork', 'name': row['title'],
                          'description': row['summary'],
                          **({'alternateName': row['cooking_title']} if row.get('cooking_title') else {})}}
                for index, row in enumerate(rows, 1)]}}
    # JSON inside an HTML script is raw text: prevent a catalog value from
    # closing the element or introducing markup, while preserving JSON values.
    payload = json.dumps(data, ensure_ascii=False, indent=2)
    for character, escaped in (('<', r'\u003c'), ('>', r'\u003e'), ('&', r'\u0026')):
        payload = payload.replace(character, escaped)
    return '<script type="application/ld+json">\n' + payload + '\n</script>'


def build():
    rows = catalog()
    # Validate every source before writing any generated artifact.
    for row in rows:
        if row['status'] == 'snapshot':
            package_files(row)
    for host in ('codex', 'claude'):
        plugin_files(host)
    site = ROOT / 'site'
    (site / 'downloads').mkdir(parents=True, exist_ok=True)
    cards, sums = [], []
    labels = ('Wann kochen?', 'Zutaten', 'Zubereitung', 'Abschmecken', 'Servieren')
    for index, row in enumerate(rows, 1):
        esc = html.escape
        slug = row['id']
        details = ''.join(f'<dt>{label}</dt><dd>{esc(row[field])}</dd>' for label, field in zip(labels, RECIPE_FIELDS))
        download = '<p>Nur Katalogkandidat · Paket nach Lizenzentscheidung.</p>'
        if row['status'] == 'snapshot':
            target = site / 'downloads' / f'{slug}.zip'
            zip_bytes(row, target)
            sums.append(f'{sha(target.read_bytes())}  {slug}.zip')
            download = f'<p><a href="downloads/{slug}.zip" download>Skill-ZIP herunterladen</a> · <a href="skills/{slug}/SKILL.md">Originalanleitung</a></p>'
        behavior = ('Gezielte Scan-Tests dokumentiert; Scannerabdeckung begrenzt' if row['id'] == 'did-i-leak' else 'Gezielte Host-Szenarien dokumentiert; keine vollständige Abnahme') if row['status'] == 'snapshot' else 'Katalogkandidat; kein Paket- oder Host-Test'
        source = row.get('repository')
        source_link = f'<a href="{esc(source, quote=True)}">Quellprojekt</a>' if source else 'Lokale eigene Quelle'
        cards.append(f'<article id="{slug}"><p class="eyebrow">{index:02d} / {esc(row["phase"])}</p><h2>{esc(row["title"])}</h2><p class="cooking-title">{esc(row["cooking_title"])}</p><p>{esc(row["summary"])}</p><p class="status">{esc(row["license"])} · {esc(row["status"])}</p><details><summary>Rezept und Grenzen</summary><dl>{details}<dt>Grenzen</dt><dd>{esc(row["limits"])}</dd><dt>Beispiel</dt><dd><code>{esc(row["prompt"])}</code></dd></dl></details>{download}<small>{source_link} · Revision {esc((row.get("revision") or "ohne Commit")[:12])}<br>{behavior}</small></article>')
    page = (ROOT / 'templates/index.html').read_text().replace('{{CARDS}}', '\n'.join(cards)).replace('{{STRUCTURED_DATA}}', schema_script(rows))
    (site / 'index.html').write_text(page)
    css = page.split('<style>')[1].split('</style>')[0]
    (site / 'help.html').write_text((ROOT / 'templates/help.html').read_text().replace('{{CSS}}', css))
    (site / 'assets').mkdir(exist_ok=True)
    shutil.copyfile(ROOT / 'assets/icon.svg', site / 'assets/icon.svg')
    shutil.copyfile(ROOT / 'LICENSE', site / 'LICENSE')
    for row in rows:
        if row['status'] == 'snapshot':
            folder, files = package_files(row)
            for name in files:
                target = site / 'skills' / row['id'] / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((folder / name).read_bytes())
    sums.extend(build_plugins(site / 'downloads'))
    build_sidebar()
    (site / 'downloads/SHA256SUMS').write_text('\n'.join(sums) + '\n')
    write_zip({str(p.relative_to(site)): p.read_bytes() for p in site.rglob('*') if p.is_file()}, ROOT / 'dist/website.zip')
    print(f'Built {len(rows)} recipes, {len(sums)} deterministic ZIPs (including 2 plugin bundles)')


def check():
    rows = catalog()
    check_plugins()
    for row in rows:
        if row['status'] == 'snapshot':
            folder, files = package_files(row)
            target = ROOT / 'site/downloads' / f'{row["id"]}.zip'
            with zipfile.ZipFile(target) as archive:
                expected = {f'{row["id"]}/{name}' for name in files}
                if set(archive.namelist()) != expected or archive.testzip():
                    raise ValueError('Invalid ZIP contents')
                for name in files:
                    if archive.read(f'{row["id"]}/{name}') != (folder / name).read_bytes():
                        raise ValueError('ZIP differs from snapshot')
    bundle = json.loads((ROOT / 'bundle.json').read_text())
    expected_downloads = {f'{r["id"]}.zip' for r in rows if r['status'] == 'snapshot'}
    expected_downloads.update(f'{bundle["name"]}-{host}.zip' for host in ('codex', 'claude'))
    lines = (ROOT / 'site/downloads/SHA256SUMS').read_text().splitlines()
    if len(lines) != len(expected_downloads) or {line.split('  ')[1] for line in lines} != expected_downloads:
        raise ValueError('Incomplete or unexpected checksum entries')
    if {p.name for p in (ROOT / 'site/downloads').glob('*.zip')} != expected_downloads:
        raise ValueError('Unexpected stale download; review generated output')
    for line in lines:
        digest, name = line.split('  ')
        if sha((ROOT / 'site/downloads' / name).read_bytes()) != digest:
            raise ValueError('ZIP checksum mismatch')
    for paths in ([ROOT / 'README.md'], (ROOT / 'docs').rglob('*'), (ROOT / 'skills').rglob('*'), (ROOT / 'site').rglob('*')):
        for path in paths:
            if path.suffix not in ('.md', '.html'):
                continue
            text = path.read_text()
            links = re.findall(r'\[[^\]]*\]\(([^)]+)\)', text) if path.suffix == '.md' else re.findall(r'(?:href|src)="([^"]+)"', text)
            for link in links:
                if re.match(r'^[a-zA-Z][\w+.-]*:', link) or link.startswith('#'):
                    continue
                local = link.split('#')[0]
                if local and not (path.parent / local).exists():
                    raise ValueError(f'Broken link: {path.relative_to(ROOT)} -> {link}')
    print('OK: metadata, snapshot hashes, individual/plugin ZIPs, marketplaces, checksums, local links')


def check_sources():
    registry = json.loads((ROOT / 'sources.local.json').read_text())
    drift = []
    for row in catalog():
        for name, digest in row['files'].items():
            path = Path(registry[row['id']]) / name
            if not path.is_file() or sha(path.read_bytes()) != digest:
                drift.append(f'{row["id"]}/{name}')
    if drift:
        raise ValueError('Source drift; review before updating: ' + ', '.join(drift))
    print('OK: snapshot files still match configured originals')


def install(slug, destination):
    row = next((r for r in catalog() if r['id'] == slug), None)
    if not row or row['status'] != 'snapshot':
        raise ValueError('No installable snapshot for this ID')
    folder, _ = package_files(row)
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / slug
    if target.exists() or target.is_symlink():
        raise ValueError('Existing skill preserved; choose an empty destination')
    shutil.copytree(folder, target)
    print(f'Installed snapshot: {target}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('build', 'check', 'check-sources', 'serve'):
        sub = commands.add_parser(name)
        if name == 'serve':
            sub.add_argument('--port', type=int, default=8766)
    sub = commands.add_parser('install')
    sub.add_argument('id')
    sub.add_argument('--dest', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == 'build':
            build()
        elif args.command == 'check':
            check()
        elif args.command == 'install':
            install(args.id, args.dest.expanduser())
        elif args.command == 'check-sources':
            check_sources()
        else:
            build()
            # Expose only this repository's shareable content; deny private state.
            class Handler(http.server.SimpleHTTPRequestHandler):
                def do_GET(self):
                    from urllib.parse import unquote, urlsplit
                    parts = Path(unquote(urlsplit(self.path).path)).parts
                    allowed = {'site', 'skills', 'docs', 'catalog.json', 'README.md', 'LICENSE'}
                    if len(parts) < 2 or parts[1] not in allowed or any(p.startswith('.') for p in parts) or '..' in parts:
                        self.send_error(403)
                        return
                    super().do_GET()

                do_HEAD = do_GET
            handler = lambda *a, **kw: Handler(*a, directory=str(ROOT), **kw)
            print(f'Private preview: http://127.0.0.1:{args.port}/site/', flush=True)
            with http.server.ThreadingHTTPServer(('127.0.0.1', args.port), handler) as server:
                server.serve_forever()
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as error:
        parser.error(str(error))


if __name__ == '__main__':
    main()
