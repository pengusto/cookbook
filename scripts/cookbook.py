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
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
RECIPE_FIELDS = ('when', 'ingredients', 'steps', 'verify', 'result')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def catalog():
    rows = json.loads((ROOT / 'catalog.json').read_text())
    ids = set()
    installed = {'plain': set(), 'kitchen': set()}
    for row in rows:
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', row['id']) or row['id'] in ids:
            raise ValueError('Invalid or duplicate recipe ID')
        ids.add(row['id'])
        if set(row.get('install_ids', {})) != {'plain', 'kitchen'}:
            raise ValueError('Both naming variants require an invocation ID')
        for variant, name in row['install_ids'].items():
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or name in installed[variant]:
                raise ValueError('Invalid or duplicate installed skill ID')
            installed[variant].add(name)
        if any(not row[field].strip() for field in (*RECIPE_FIELDS, 'title', 'cooking_title')):
            raise ValueError('Incomplete recipe')
        if row['status'] not in ('source', 'candidate'):
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


VARIANTS = ('plain', 'kitchen')


def rendered_files(row, variant):
    if variant not in VARIANTS:
        raise ValueError('Unknown naming variant')
    folder, files = package_files(row)
    slug = row['install_ids'][variant]
    title = row['title'] if variant == 'plain' else row['cooking_title']
    result = {name: (folder / name).read_bytes() for name in files}
    for name in ('SKILL.md', 'agents/openai.yaml'):
        text = result[name].decode().replace('{{TITLE}}', title).replace('{{ID}}', slug)
        if name == 'SKILL.md':
            text = re.sub(r'(?m)^name: .+$', 'name: ' + slug, text, count=1)
        if '{{' in text:
            raise ValueError('Unresolved skill template')
        result[name] = text.encode()
    return slug, result


def zip_bytes(row, target, variant='plain'):
    slug, files = rendered_files(row, variant)
    write_zip({f'{slug}/{name}': data for name, data in files.items()}, target)


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


def plugin_files(host, variant='plain'):
    if variant not in VARIANTS:
        raise ValueError('Unknown naming variant')
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
        listing['displayName'] = config['display_name']
        listing['shortDescription'] = 'Plain questions' if variant == 'plain' else 'Kitchen names'
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
        manifest['displayName'] = config['display_name']
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
        if not row or row['status'] != 'source':
            raise ValueError(f'Bundle requires a reviewed installable snapshot: {slug}')
        install_id, rendered = rendered_files(row, variant)
        files.update({f'skills/{install_id}/{name}': data for name, data in rendered.items()})
        sources.append({key: row[key] for key in ('id', 'license', 'repository', 'revision', 'files')})
    files['SOURCES.json'] = json_bytes({'bundle': config['name'], 'version': config['version'], 'variant': variant, 'skills': sources})
    files['README.md'] = (ROOT / 'templates/plugin-README.md').read_text().replace('{{VARIANT}}', variant).encode()
    files['README.de.md'] = (ROOT / 'templates/plugin-README.de.md').read_text().replace('{{VARIANT}}', variant).encode()
    return config, files


def marketplace(host, config):
    name = config['name']
    if host == 'codex':
        return '.agents/plugins/marketplace.json', {
            'name': 'cookbook-by-pengusto-local', 'plugins': [{
                'name': name, 'source': {'source': 'local', 'path': f'./plugins/{name}'},
                'policy': {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'},
                'category': 'Developer Tools'}]}
    return '.claude-plugin/marketplace.json', {
        'name': 'cookbook-by-pengusto-local', 'owner': config['author'],
        'metadata': {'description': 'Local review marketplace for the selected Cookbook skills.'},
        'plugins': [{'name': name, 'source': f'./plugins/{name}', 'description': config['description']}]}


def build_plugins(downloads):
    sums = []
    for variant in VARIANTS:
        for host in ('codex', 'claude'):
            config, files = plugin_files(host, variant)
            root = ROOT / 'dist' / variant / host
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
            target = downloads / f'{config["name"]}-{variant}-{host}.zip'
            archive_files = {f'{config["name"]}/plugins/{config["name"]}/{name}': data for name, data in files.items()}
            archive_files[f'{config["name"]}/{name}'] = json_bytes(value)
            write_zip(archive_files, target)
            sums.append(f'{sha(target.read_bytes())}  {target.name}')
    return sums


def sidebar_files(variant='plain'):
    """Optional read-only companion; does not duplicate installed skills."""
    name = 'cookbook-sidebar'
    listing = json.loads((ROOT / 'store/listing.json').read_text())
    listing.update(displayName='Cookbook by Pengusto', shortDescription='Browse local skill recipes',
                   longDescription='Read the local Cookbook catalog in the sidebar. Requires Python 3.10+. Does not install skills, edit files, or publish.',
                   capabilities=['Browse the local Cookbook'], defaultPrompt=[])
    manifest = {'name': name, 'version': '0.2.0', 'description': listing['longDescription'],
                'author': {'name': 'Pengusto'}, 'license': 'MIT', 'interface': listing,
                'mcpServers': './.mcp.json'}
    config = {'mcpServers': {name: {'command': 'python3',
              'args': ['./scripts/sidebar_server.py'], 'cwd': './'}}}
    cards = []
    for row in catalog():
        row = dict(row, title=row['title'] if variant == 'plain' else row['cooking_title'])
        esc = html.escape
        fields = ''.join(f'<dt>{esc(key)}</dt><dd>{esc(row[key])}</dd>'
                         for key in (*RECIPE_FIELDS, 'limits'))
        cards.append(f'<article><p class="eyebrow">{esc(row["phase"])}</p><h2>{esc(row["title"])}</h2>'
                     f'<p>{esc(row["summary"])}</p><p class="status">{esc(row["license"])} · {esc(row["status"])}</p>'
                     f'<details><summary>Rezept öffnen</summary><dl>{fields}</dl>'
                     f'<p>Beispielaufruf für einen separat installierten Skill:</p><code>{esc(row["prompt"])}</code></details></article>')
    css = (ROOT / 'assets/sidebar.css').read_text()
    bridge = '''<script>
const initId = 'cookbook-init';
addEventListener('message', event => {
  if (event.source !== parent || !event.data || event.data.jsonrpc !== '2.0') return;
  if (event.data.id === initId && event.data.result) {
    parent.postMessage({jsonrpc:'2.0',method:'ui/notifications/initialized'}, '*');
  }
});
parent.postMessage({jsonrpc:'2.0',id:initId,method:'ui/initialize',params:{protocolVersion:'2026-01-26',appInfo:{name:'cookbook-sidebar',version:'0.2.0'},appCapabilities:{}}}, '*');
</script>'''
    page = '<!doctype html><html lang="de"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    page += f'<title>Cookbook</title><style>{css}</style><header><p class="eyebrow">Lokales Cookbook</p><h1>Cookbook by Pengusto</h1>'
    page += '<p>Sieben Rezepte, sieben separat installierbare Skills. Diese Ansicht ist zum Lesen; sie installiert oder veröffentlicht nichts.</p></header>'
    page += '<main><div class="grid">' + ''.join(cards) + '</div></main>' + bridge + '</html>'
    files = {'.codex-plugin/plugin.json': json_bytes(manifest), '.mcp.json': json_bytes(config),
             'scripts/sidebar_server.py': (ROOT / 'scripts/sidebar_server.py').read_bytes(),
             'ui/index.html': page.encode(), 'LICENSE': (ROOT / 'LICENSE').read_bytes()}
    for asset in ('icon.png', 'icon-dark.png', 'icon.svg', 'icon-dark.svg', 'sidebar-icon.svg'):
        files[f'assets/{asset}'] = (ROOT / 'assets' / asset).read_bytes()
    return files


def build_sidebar(variant='plain'):
    root = ROOT / 'dist' / variant / 'sidebar'
    files = sidebar_files(variant)
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
    for variant in VARIANTS:
        for host in ('codex', 'claude'):
            config, files = plugin_files(host, variant)
            root = ROOT / 'dist' / variant / host
            plugin = root / 'plugins' / config['name']
            actual = {str(p.relative_to(plugin)): p.read_bytes() for p in plugin.rglob('*') if p.is_file()}
            if actual != files:
                raise ValueError('Generated plugin differs from canonical source')
            market_path, value = marketplace(host, config)
            if (root / market_path).read_bytes() != json_bytes(value):
                raise ValueError('Marketplace configuration differs')
            with zipfile.ZipFile(ROOT / 'site/downloads' / f'{config["name"]}-{variant}-{host}.zip') as archive:
                expected = {f'{config["name"]}/plugins/{config["name"]}/{name}': data for name, data in files.items()}
                expected[f'{config["name"]}/{market_path}'] = json_bytes(value)
                if {name: archive.read(name) for name in archive.namelist()} != expected:
                    raise ValueError('Plugin archive differs')


def schema_script(rows, language="de"):
    """Describe only the visible collection; omit unconfirmed public identifiers."""
    data = {
        '@context': 'https://schema.org', '@type': 'CollectionPage',
        'name': 'Cookbook by Pengusto', 'inLanguage': language,
        'mainEntity': {
            '@type': 'ItemList', 'numberOfItems': len(rows),
            'itemListElement': [
                {'@type': 'ListItem', 'position': index,
                 'item': {'@type': 'CreativeWork', 'name': row['title'],
                          'description': row['summary']}}
                for index, row in enumerate(rows, 1)]}}
    # JSON inside an HTML script is raw text: prevent a catalog value from
    # closing the element or introducing markup, while preserving JSON values.
    payload = json.dumps(data, ensure_ascii=False, indent=2)
    for character, escaped in (('<', r'\u003c'), ('>', r'\u003e'), ('&', r'\u0026')):
        payload = payload.replace(character, escaped)
    return '<script type="application/ld+json">\n' + payload + '\n</script>'



def page_name(language, variant):
    return ('index' if variant == 'plain' else 'kitchen') + ('' if language == 'de' else '-en') + '.html'


def render_landing(rows, language, variant):
    translations = json.loads((ROOT / 'templates/locales.json').read_text())
    ui = translations[language]
    esc = html.escape
    visible, cards = [], []
    icons = ('clipboard', 'soup', 'lock', 'search', 'bell', 'list-details', 'door-exit')
    def icon(name):
        return f'<span class="ui-icon icon-{name}" aria-hidden="true"></span>'
    for index, row in enumerate(rows):
        title = row['title'] if variant == 'plain' else row['cooking_title']
        fields = dict(row, **ui.get('skills', {}).get(row['id'], {}))
        visible.append(dict(fields, title=title))
        slug = row['install_ids'][variant]
        definition = ''.join(f'<dt>{esc(ui[key])}</dt><dd>{esc(fields[key])}</dd>' for key in (*RECIPE_FIELDS, 'limits'))
        cards.append(f'<article class="skill" id="{row["id"]}"><details><summary><span class="skill-number" aria-hidden="true">{index + 1:02d}</span><span class="skill-icon" aria-hidden="true">{icon(icons[index])}</span><h2>{esc(title)}</h2><p>{esc(fields["summary"])}</p><span class="row-arrow" aria-hidden="true">{icon("arrow-right")}</span></summary><div class="skill-body"><dl>{definition}</dl><div class="skill-links"><code>${slug}</code><a href="downloads/{variant}-{row["id"]}.zip" download>{icon("download")}{esc(ui["ZIP"])}</a><a href="skills/{variant}/{slug}/SKILL.md">{esc(ui["GUIDE"])}</a></div></div></details></article>')
    hosts = []
    for host, title in (('codex', 'Codex'), ('claude', 'Claude Code')):
        commands = (f'codex plugin marketplace add .\ncodex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local' if host == 'codex' else 'claude plugin marketplace add . --scope user\nclaude plugin install cookbook-by-pengusto@cookbook-by-pengusto-local --scope user')
        hosts.append(f'<div class="host"><h3>{icon("terminal-2")}{title}</h3><a class="download" href="downloads/cookbook-by-pengusto-{variant}-{host}.zip" download>{icon("download")}{esc(ui["DOWNLOAD"])}</a><p>{esc(ui["EXTRACT"])}</p><pre><code>{esc(commands)}</code></pre><p class="small">{esc(ui["NEW_SESSION"])}</p></div>')
    variant_links = ''.join(f'<a href="{page_name(language, v)}#skills"' + (' aria-current="page"' if v == variant else '') + f'>{icon("chef-hat" if v == "kitchen" else "message-circle")}{esc(ui[v.upper()])}</a>' for v in ('kitchen', 'plain'))
    lang_links = ''.join(f'<a href="{page_name(lang, variant)}" lang="{lang}" hreflang="{lang}"' + (' aria-current="page"' if lang == language else '') + f'>{lang.upper()}</a>' for lang in ('de', 'en'))
    values = {key: esc(value) for key, value in ui.items() if isinstance(value, str)}
    values.update(LANG=language, HOME=page_name(language, variant), HELP='help.html' if language == 'de' else 'help-en.html',
                  CARDS='\n'.join(cards), HOSTS=''.join(hosts), VARIANT_LINKS=variant_links, LANG_LINKS=lang_links,
                  CURRENT_VARIANT=esc(ui[variant.upper()]), STRUCTURED_DATA=schema_script(visible, language),
                  ASSET_VERSION=sha((ROOT / 'assets/site.css').read_bytes() + (ROOT / 'assets/cookbook-hero-transparent.png').read_bytes())[:12])
    template = (ROOT / 'templates/index.html').read_text()
    page = re.sub(r'\{\{([A-Z0-9_]+)\}\}', lambda match: values[match[1]], template)
    if '{{' in page:
        raise ValueError('Unresolved website placeholder')
    return page

def build():
    rows = catalog()
    for row in rows:
        if row['status'] == 'source':
            package_files(row)
    for variant in VARIANTS:
        for host in ('codex', 'claude'):
            plugin_files(host, variant)
    site = ROOT / 'site'
    (site / 'downloads').mkdir(parents=True, exist_ok=True)
    sums = []
    for variant in VARIANTS:
        for row in rows:
            slug, files = rendered_files(row, variant)
            target = site / 'downloads' / f'{variant}-{row["id"]}.zip'
            write_zip({f'{slug}/{name}': data for name, data in files.items()}, target)
            sums.append(f'{sha(target.read_bytes())}  {target.name}')
            for name, data in files.items():
                path = site / 'skills' / variant / slug / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
        for language in ('de', 'en'):
            (site / page_name(language, variant)).write_text(render_landing(rows, language, variant))
        build_sidebar(variant)
    for language in ('de', 'en'):
        (site / ('help.html' if language == 'de' else 'help-en.html')).write_text((ROOT / 'templates' / ('help.html' if language == 'de' else 'help-en.html')).read_text())
    (site / 'assets').mkdir(exist_ok=True)
    # Remove obsolete generated copies; preserve the original source images.
    for name in ('cookbook-hero.jpg', 'cookbook-hero-dark.jpg'):
        (site / 'assets' / name).unlink(missing_ok=True)
    for name in ('icon.svg', 'icon-dark.svg', 'site.css', 'cookbook-hero-transparent.png'):
        shutil.copyfile(ROOT / 'assets' / name, site / 'assets' / name)
    shutil.copytree(ROOT / 'assets/icons', site / 'assets/icons', dirs_exist_ok=True)
    shutil.copyfile(ROOT / 'LICENSE', site / 'LICENSE')
    sums.extend(build_plugins(site / 'downloads'))
    (site / 'downloads/SHA256SUMS').write_text('\n'.join(sums) + '\n')
    write_zip({str(p.relative_to(site)): p.read_bytes() for p in site.rglob('*') if p.is_file()}, ROOT / 'dist/website.zip')
    print(f'Built {len(rows)} shared sources, two naming variants, {len(sums)} ZIPs')


def check():
    rows = catalog()
    check_plugins()
    expected_downloads = {f'{v}-{row["id"]}.zip' for row in rows for v in VARIANTS}
    expected_downloads.update(f'cookbook-by-pengusto-{v}-{h}.zip' for v in VARIANTS for h in ('codex', 'claude'))
    for row in rows:
        for variant in VARIANTS:
            slug, files = rendered_files(row, variant)
            with zipfile.ZipFile(ROOT / 'site/downloads' / f'{variant}-{row["id"]}.zip') as archive:
                if {n: archive.read(n) for n in archive.namelist()} != {f'{slug}/{n}': data for n, data in files.items()}:
                    raise ValueError('Individual ZIP differs from canonical source')
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
                local = urlsplit(link).path
                if local and not (path.parent / local).exists():
                    raise ValueError(f'Broken link: {path.relative_to(ROOT)} -> {link}')
    print('OK: metadata, snapshot hashes, individual/plugin ZIPs, marketplaces, checksums, local links')


def check_sources():
    for row in catalog():
        package_files(row)
    print('OK: seven canonical sources and reviewed runtime hashes; no external source dependency')


def install(slug, destination, variant='plain'):
    row = next((r for r in catalog() if r['id'] == slug), None)
    if not row or row['status'] != 'source':
        raise ValueError('No installable source for this ID')
    name, files = rendered_files(row, variant)
    destination.mkdir(parents=True, exist_ok=True)
    # Prevent parallel naming variants of the same workflow in one destination.
    if any((destination / alias).exists() or (destination / alias).is_symlink() for alias in {slug, *row['install_ids'].values()}):
        raise ValueError('Existing skill preserved; choose an empty destination')
    target = destination / name
    for path, data in files.items():
        p = target / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
        p.chmod(0o755 if path.startswith('bin/') else 0o644)
    print(f'Installed {variant} skill: {target}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('build', 'check', 'check-sources', 'serve'):
        sub = commands.add_parser(name)
        if name == 'serve':
            sub.add_argument('--port', type=int, default=8766)
    sub = commands.add_parser('install')
    sub.add_argument('id')
    sub.add_argument('--variant', choices=VARIANTS, required=True)
    sub.add_argument('--dest', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == 'build':
            build()
        elif args.command == 'check':
            check()
        elif args.command == 'install':
            install(args.id, args.dest.expanduser(), args.variant)
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
