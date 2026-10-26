#!/usr/bin/env python3
"""Build and verify curated skill snapshots; never execute skill instructions."""
import argparse
import base64
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
PUBLIC_BASE = 'https://pengusto.github.io/cookbook/'
RECIPE_FIELDS = ('when', 'ingredients', 'steps', 'verify', 'result')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def catalog():
    rows = json.loads((ROOT / 'catalog.json').read_text())
    ids = set()
    chapters = []
    installed = {'plain': set(), 'kitchen': set()}
    for row in rows:
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', row['id']) or row['id'] in ids:
            raise ValueError('Invalid or duplicate recipe ID')
        ids.add(row['id'])
        chapter = row.get('chapter', '')
        if not re.fullmatch(r'[a-z]+(?:-[a-z]+)*', chapter):
            raise ValueError('Missing or invalid chapter ID')
        if not chapters or chapter != chapters[-1]:
            if chapter in chapters:
                raise ValueError('Recipes in each chapter must be contiguous')
            chapters.append(chapter)
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
    for name in ('SKILL.md', 'agents/openai.yaml', *(['examples.md'] if 'examples.md' in result else [])):
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
    if config['store_variant'] not in VARIANTS:
        raise ValueError('Unknown store naming variant')
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
    invocations = []
    for slug in selected:
        row = rows[slug]
        title = row['title'] if variant == 'plain' else row['cooking_title']
        name = row['install_ids'][variant]
        command = f'${name}' if host == 'codex' else f'/{config["name"]}:{name}'
        invocations.append(f'| {title} | `{command}` |')
    for language in ('', '.de'):
        text = (ROOT / f'templates/plugin-README{language}.md').read_text()
        for key, value in {'VERSION': config['version'], 'VARIANT': variant,
                           'HOST': 'Codex' if host == 'codex' else 'Claude Code',
                           'COUNT': str(len(selected)), 'INVOCATIONS': '\n'.join(invocations)}.items():
            text = text.replace('{{' + key + '}}', value)
        files[f'README{language}.md'] = text.encode()
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
            if host == 'codex':
                # Portal uploads contain the plugin itself, not a marketplace wrapper.
                upload = ROOT / 'dist' / 'store' / variant / f'{config["name"]}.zip'
                upload.parent.mkdir(parents=True, exist_ok=True)
                write_zip(files, upload)
            sums.append(f'{sha(target.read_bytes())}  {target.name}')
    return sums


def recipe_icons():
    """One meaningful utensil per shared workflow, independent of naming or order."""
    import xml.etree.ElementTree as ET
    icons = json.loads((ROOT / 'ui/recipe-icons.json').read_text())
    if set(icons) != {row['id'] for row in catalog()}:
        raise ValueError('Recipe icons must cover the exact catalog')
    if len({icon['id'] for icon in icons.values()}) != len(icons):
        raise ValueError('Every recipe needs its own distinct utensil')
    for icon in icons.values():
        if not re.fullmatch('[a-z]+(?:-[a-z]+)*', icon['id']) or not icon['meaning'].strip():
            raise ValueError('Invalid recipe icon identity')
        svg = ET.fromstring('<svg>' + icon['body'] + '</svg>')
        if any(node.tag not in ('svg', 'path', 'circle', 'rect', 'ellipse') or any(key not in ('d','x','y','width','height','rx','cx','cy','r','ry') for key in node.attrib) for node in svg.iter()):
            raise ValueError('Recipe icons may only contain static drawing geometry')
    return icons


def food_image_style(row):
    """Square, padded cutouts use contain; sheet coordinates never reach the UI."""
    props = {}
    for key, record in [('dish', row['cutouts']['dish']), *[(f'cell{i}', r) for i,r in enumerate(row['cutouts']['ingredients'])]]:
        content = (ROOT / 'assets/cookbook/food' / record['file']).read_bytes()
        props['--food-'+key+'-image'] = "url('data:image/webp;base64," + base64.b64encode(content).decode() + "')"
    return props


def food_art():
    rows = json.loads((ROOT / 'assets/cookbook/food/SOURCES.json').read_text())
    expected = {row['id'] for row in catalog()} | {'welcome', 'install', 'about'}
    if len(rows) != len(expected) or {row['id'] for row in rows} != expected:
        raise ValueError('Each recipe and information page needs its own food illustration')
    for row in rows:
        if row['file'] != row['id'] + '.webp' or len(row['ingredients']) != 4:
            raise ValueError('Invalid food sheet contract')
        cutouts = row['cutouts']
        if len(cutouts['ingredients']) != 4:
            raise ValueError('Each dish needs four separate ingredient images')
        for record in [cutouts['dish'], *cutouts['ingredients']]:
            path = Path(record['file'])
            if path.parent != Path('cutouts') or path.suffix != '.webp' or record['size'][0] != record['size'][1]:
                raise ValueError('Food cutouts must be local square WebP files')
            if sha((ROOT / 'assets/cookbook/food' / path).read_bytes()) != record['sha256']:
                raise ValueError('Food cutout hash mismatch')
        if sha((ROOT / 'assets/cookbook/food' / row['file']).read_bytes()) != row['sha256']:
            raise ValueError('Food illustration hash mismatch')
    if len({row['sha256'] for row in rows}) != len(rows):
        raise ValueError('Food illustrations must be different per page')
    return {row['id']: row for row in rows}


def sidebar_files(variant='plain'):
    """Optional read-only companion; does not duplicate installed skills."""
    name = 'cookbook-sidebar'
    listing = json.loads((ROOT / 'store/listing.json').read_text())
    listing.update(displayName='Cookbook by Pengusto', shortDescription='Browse local skill recipes',
                   longDescription='Read the local Cookbook catalog in the sidebar. Requires Python 3.10+. Does not install skills, edit files, or publish.',
                   capabilities=['Browse the local Cookbook'], defaultPrompt=[])
    manifest = {'name': name, 'version': json.loads((ROOT / 'bundle.json').read_text())['sidebar_version'], 'description': listing['longDescription'],
                'author': {'name': 'Pengusto'}, 'license': 'MIT', 'interface': listing,
                'mcpServers': './.mcp.json'}
    config = {'mcpServers': {name: {'command': 'python3',
              'args': ['./scripts/sidebar_server.py'], 'cwd': './'}}}
    import base64
    def data_uri(path, mime):
        return 'data:' + mime + ';base64,' + base64.b64encode((ROOT / path).read_bytes()).decode()
    locales = json.loads((ROOT / 'ui/locales.json').read_text())
    expected = {'de', 'en', 'fr', 'es', 'pt-BR', 'it', 'tr', 'ja', 'ko', 'zh-CN', 'ar', 'hi'}
    if set(locales) != expected:
        raise ValueError('Cookbook UI requires the twelve reviewed locales')
    recipe_count = len(catalog())
    chapter_ids = list(dict.fromkeys(row['chapter'] for row in catalog()))
    reference_keys = set(locales['de'])
    for locale, values in locales.items():
        if set(values) != reference_keys or any(not str(value).strip() for value in values.values()):
            raise ValueError(f'Incomplete UI locale: {locale}')
        if set(values['chapterTitles']) != set(chapter_ids) or any(not title.strip() for title in values['chapterTitles'].values()):
            raise ValueError(f'Incomplete chapter titles: {locale}')
        for key in ('summaries', 'whenList', 'intros'):
            if len(values[key].split('|')) != recipe_count:
                raise ValueError(f'Incomplete recipes: {locale}/{key}')
        if len(values['recipeLimits']) != recipe_count or len(values['stepNotes']) != 4 or len(values['verifications']) != recipe_count or len(values['ingredientLists']) != recipe_count or any(len(row) != 4 for row in values['ingredientLists']):
            raise ValueError(f'Incomplete recipe details: {locale}')
        if any(len(values['steps'+str(i)].split('|')) != 4 for i in range(recipe_count)):
            raise ValueError(f'Incomplete preparation steps: {locale}')
    accents = ['#795132', '#8a523d', '#8b522d', '#465e70', '#843327', '#326b70', '#69712c', '#936231', '#52623e', '#84602e', '#6e713b', '#58716a', '#6d405d', '#78602e', '#3f6963', '#9b4f30', '#3f536a', '#774551']
    dark_accents = ['#ddc19b', '#e7b49d', '#e1b88d', '#a9c8dc', '#e3a384', '#96d5da', '#cbd58e', '#e9c08a', '#b9cd92', '#e9c481', '#d0d59b', '#aacfc3', '#d5add0', '#e6ca87', '#9fd1c6', '#ecb08b', '#b5c9e1', '#e5a5b8']
    utensil_icons = recipe_icons()
    food = food_art()
    recipes = [{'icon': utensil_icons[row['id']]['id'], 'id': row['install_ids'][variant], 'sourceId': row['id'], 'title': row['title'] if variant == 'plain' else row['cooking_title'],
                'names': {'plain': row['title'], 'kitchen': row['cooking_title']}, 'installIds': row['install_ids'], 'chapter': row['chapter'],
                'accent': accents[index], 'accentDark': dark_accents[index], 'dishNames': food[row['id']]['dishNames'], 'artwork': food_image_style(food[row['id']])}
               for index, row in enumerate(catalog())]
    payload = json.dumps({'version': manifest['version'], 'variant': variant, 'recipes': recipes, 'locales': locales}, ensure_ascii=False).replace('<', '\\u003c')
    css = (ROOT / 'assets/sidebar.css').read_text() + '\n' + (ROOT / 'assets/vendor/lenis/lenis.css').read_text()
    font_css = []
    for font in json.loads((ROOT / 'assets/vendor/fonts/sources.json').read_text()):
        block = font['css'].replace('Caveat', 'CookbookHand').replace('Cormorant Garamond', 'CookbookSerif')
        block = block.replace(font['source'], data_uri('assets/vendor/fonts/' + font['family'] + '/' + font['file'], 'font/woff2'))
        font_css.append(block)
    css = css.replace('/*COOKBOOK_FONTS*/', '\n'.join(font_css))
    css = css.replace('DECOR_ASSET', data_uri('assets/cookbook/decor.webp', 'image/webp'))
    page = (ROOT / 'ui/book.html').read_text()
    page = page.replace('<!--RECIPE_ICONS-->', ''.join('<symbol id="recipe-'+icon['id']+'" viewBox="0 0 32 32">'+icon['body']+'</symbol>' for icon in utensil_icons.values()))
    for token, content in (
        ('/*COOKBOOK_CSS*/', css), ('PAN_ASSET', 'data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22/%3E'),
        ('/*COOKBOOK_DATA*/', payload),
        ('/*COOKBOOK_MOTION*/', (ROOT / 'assets/vendor/animejs/anime.umd.min.js').read_text()),
        ('/*COOKBOOK_LENIS*/', (ROOT / 'assets/vendor/lenis/lenis.min.js').read_text()),
        ('/*COOKBOOK_JS*/', (ROOT / 'ui/book.js').read_text().replace('/*COOKBOOK_SCROLL_GESTURE*/', (ROOT / 'ui/scroll-gesture.js').read_text()))):
        page = page.replace(token, content)
    files = {'.codex-plugin/plugin.json': json_bytes(manifest), '.mcp.json': json_bytes(config),
             'scripts/sidebar_server.py': (ROOT / 'scripts/sidebar_server.py').read_bytes(),
             'ui/index.html': page.encode(), 'LICENSE': (ROOT / 'LICENSE').read_bytes()}
    for source, target in (
        ('assets/vendor/animejs/LICENSE.md', 'licenses/animejs.txt'),
        ('assets/vendor/lenis/LICENSE', 'licenses/lenis.txt'),
        ('assets/vendor/lenis/SOURCE.json', 'licenses/lenis-source.json'),
        ('assets/vendor/animejs/SOURCE.json', 'licenses/animejs-source.json'),
        ('assets/vendor/fonts/cormorantgaramond/OFL.txt', 'licenses/cormorant-garamond.txt'),
        ('assets/vendor/fonts/caveat/OFL.txt', 'licenses/caveat.txt')):
        files[target] = (ROOT / source).read_bytes()
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


def schema_script(rows, language="de", chapter_titles=None):
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
    if chapter_titles is not None:
        data['hasPart'] = [
            {'@type': 'CreativeWork', 'identifier': chapter,
             'name': chapter_titles[chapter],
             'hasPart': [entry['item'] for row, entry in zip(rows, data['mainEntity']['itemListElement'])
                         if row['chapter'] == chapter]}
            for chapter in dict.fromkeys(row['chapter'] for row in rows)]
    # JSON inside an HTML script is raw text: prevent a catalog value from
    # closing the element or introducing markup, while preserving JSON values.
    payload = json.dumps(data, ensure_ascii=False, indent=2)
    for character, escaped in (('<', r'\u003c'), ('>', r'\u003e'), ('&', r'\u0026')):
        payload = payload.replace(character, escaped)
    return '<script type="application/ld+json">\n' + payload + '\n</script>'



def page_name(language, variant):
    return ('install-plain' if variant == 'plain' else 'install') + ('' if language == 'de' else '-en') + '.html'


def render_landing(rows, language, variant):
    translations = json.loads((ROOT / 'templates/locales.json').read_text())
    ui = translations[language]
    esc = html.escape
    visible, cards = [], []
    utensil_icons = recipe_icons()
    def icon(name):
        return f'<span class="ui-icon icon-{name}" aria-hidden="true"></span>'
    for index, row in enumerate(rows):
        title = row['title'] if variant == 'plain' else row['cooking_title']
        fields = dict(row, **ui.get('skills', {}).get(row['id'], {}))
        visible.append(dict(fields, title=title))
        slug = row['install_ids'][variant]
        definition = ''.join(f'<dt>{esc(ui[key])}</dt><dd>{esc(fields[key])}</dd>' for key in (*RECIPE_FIELDS, 'limits'))
        recipe_svg = '<svg class="recipe-utensil" viewBox="0 0 32 32" aria-hidden="true">'+utensil_icons[row['id']]['body']+'</svg>'
        cards.append(f'<article class="skill" id="{row["id"]}"><details><summary><span class="skill-number" aria-hidden="true">{index + 1:02d}</span><span class="skill-icon" aria-hidden="true">{recipe_svg}</span><h2>{esc(title)}</h2><p>{esc(fields["summary"])}</p><span class="row-arrow" aria-hidden="true">{icon("arrow-right")}</span></summary><div class="skill-body"><dl>{definition}</dl><div class="skill-links"><code>${slug}</code><a href="downloads/{variant}-{row["id"]}.zip" download>{icon("download")}{esc(ui["ZIP"])}</a><a href="skills/{variant}/{slug}/SKILL.md">{esc(ui["GUIDE"])}</a></div></div></details></article>')
    hosts = []
    for host, title in (('codex', 'Codex'), ('claude', 'Claude Code')):
        commands = (f'codex plugin marketplace add pengusto/cookbook --ref {variant}\ncodex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local' if host == 'codex' else 'claude plugin marketplace add . --scope user\nclaude plugin install cookbook-by-pengusto@cookbook-by-pengusto-local --scope user')
        install_note = ui['EXTRACT'] if host == 'claude' else ui['REMOTE_INSTALL']
        hosts.append(f'<div class="host"><h3>{icon("terminal-2")}{title}</h3><a class="download" href="downloads/cookbook-by-pengusto-{variant}-{host}.zip" download>{icon("download")}{esc(ui["DOWNLOAD"])}</a><p>{esc(install_note)}</p><pre><code>{esc(commands)}</code></pre><p class="small">{esc(ui["NEW_SESSION"])}</p></div>')
    variant_links = ''.join(f'<a href="{page_name(language, v)}#skills"' + (' aria-current="page"' if v == variant else '') + f'>{icon("chef-hat" if v == "kitchen" else "message-circle")}{esc(ui[v.upper()])}</a>' for v in ('kitchen', 'plain'))
    lang_links = ''.join(f'<a href="{page_name(lang, variant)}" lang="{lang}" hreflang="{lang}"' + (' aria-current="page"' if lang == language else '') + f'>{lang.upper()}</a>' for lang in ('de', 'en'))
    alternates = ''.join(f'<link rel="alternate" hreflang="{lang}" href="{PUBLIC_BASE}{page_name(lang, variant)}">' for lang in ('de', 'en'))
    values = {key: esc(value) for key, value in ui.items() if isinstance(value, str)}
    values.update(CANONICAL=PUBLIC_BASE+page_name(language,variant), BOOK='cookbook.html' if variant=='kitchen' else 'cookbook-plain.html', LEGAL='legal.html' if language=='de' else 'legal-en.html', POLICY='privacy.html' if language=='de' else 'privacy-en.html', LANG=language, HOME=page_name(language, variant), HELP='help.html' if language == 'de' else 'help-en.html',
                  CARDS='\n'.join(cards), HOSTS=''.join(hosts), VARIANT_LINKS=variant_links, LANG_LINKS=lang_links, ALTERNATES=alternates,
                  CURRENT_VARIANT=esc(ui[variant.upper()]), STRUCTURED_DATA=schema_script(visible, language),
                  ASSET_VERSION=sha((ROOT / 'assets/site.css').read_bytes() + (ROOT / 'assets/cookbook-hero-transparent.png').read_bytes())[:12])
    template = (ROOT / 'templates/index.html').read_text()
    page = re.sub(r'\{\{([A-Z0-9_]+)\}\}', lambda match: values[match[1]], template)
    if '{{' in page:
        raise ValueError('Unresolved website placeholder')
    return page

def public_book(variant='kitchen', language='de'):
    """Public book uses the same recipes and artwork as the offline companion."""
    page = sidebar_files(variant)['ui/index.html'].decode()
    ui = json.loads((ROOT / 'ui/public-locales.json').read_text())[language]
    config = json.loads((ROOT / 'bundle.json').read_text())
    rows = catalog()
    home = 'index.html' if language == 'de' else 'index-en.html'
    canonical = home if variant == 'kitchen' else 'cookbook-plain.html'
    values = {key: html.escape(value.replace('{count}', str(len(rows)))) for key, value in ui.items()}
    values.update(LEGAL_PAGE='legal.html' if language=='de' else 'legal-en.html', POLICY_PAGE='privacy.html' if language=='de' else 'privacy-en.html', VERSION=html.escape(config['version']), COUNT=str(len(rows)),
                  VARIANT='Kitchen' if variant == 'kitchen' else 'Plain',
                  INSTALL_FALLBACK=page_name(language, variant),
                  GUIDE_ID=next(row['install_ids'][variant] for row in rows if row['id'] == 'explain-the-cookbook'),
                  CODEX_COMMAND=html.escape('codex plugin marketplace add pengusto/cookbook --ref '+variant+'\ncodex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local'),
                  CLAUDE_COMMAND='claude plugin marketplace add . --scope user\nclaude plugin install cookbook-by-pengusto@cookbook-by-pengusto-local --scope user',
                  CODEX_ZIP='downloads/cookbook-by-pengusto-'+variant+'-codex.zip',
                  CLAUDE_ZIP='downloads/cookbook-by-pengusto-'+variant+'-claude.zip')
    import base64
    food = food_art()
    for key in ('welcome', 'install', 'about'):
        values[key.upper()+'_SPRITES'] = ';'.join(name+':'+value for name,value in food_image_style(food[key]).items())
        values[key.upper()+'_DISH'] = html.escape(food[key]['dishNames'][language])
        values[key.upper()+'_INGREDIENTS'] = ''.join('<span class="ingredient-food food-cell'+str(i)+'" role="img" aria-label="'+html.escape(name)+'"></span>' for i,name in enumerate(food[key]['ingredientNames'][language]))
    template = (ROOT / 'ui/public-pages.html').read_text()
    content = re.sub(r'\{\{([A-Z0-9_]+)\}\}', lambda m: values[m[1]], template)
    page = page.replace('<div class="recipe-spread"', content+'<div class="recipe-spread"', 1)
    nav = '<nav id="book-pages" aria-label="'+values['CONTENTS']+'">'+''.join(
        '<a href="#'+key+'" data-open-page="'+key+'">'+values[label]+'</a>'
        for key, label in (('welcome','WELCOME'),('install','INSTALL'),('about','ABOUT')))+'</nav>'
    nav += '<a class="book-install" href="#install" data-open-page="install">'+values['INSTALL']+'</a>'
    page = page.replace('<nav id="recipe-index"', nav+'<nav id="recipe-index"', 1)
    index = ''.join('<a class="recipe-tab" href="#'+row['install_ids'][variant]+'" id="'+row['install_ids'][variant]+'">'+html.escape(row['title'] if variant=='plain' else row['cooking_title'])+'</a>' for row in rows)
    page = page.replace('aria-label="Recipes"></nav>', 'aria-label="Recipes">'+index+'</nav>')
    suffix = '' if language=='de' else '-en'
    footer = '<nav class="public-book-links" aria-label="Project links"><a href="https://github.com/pengusto/cookbook">GitHub</a> · <a href="legal'+suffix+'.html">'+values['LEGAL']+'</a> · <a href="privacy'+suffix+'.html">'+values['PRIVACY']+'</a></nav>'
    page = page.replace('</aside>', footer+'</aside>')
    visible = [dict(row, title=row['title'] if variant=='plain' else row['cooking_title'],
                    summary=ui_summary) for row, ui_summary in zip(rows, json.loads((ROOT / 'ui/locales.json').read_text())[language]['summaries'].split('|'))]
    schema = schema_script(visible, language, json.loads((ROOT / 'ui/locales.json').read_text())[language]['chapterTitles']).replace('type="application/ld+json"', 'id="book-schema" type="application/ld+json"')
    fallback = '<noscript><style>[data-book-page][hidden]{display:grid!important}[data-host-panel][hidden]{display:block!important}#recipe-content{display:none}</style><section class="book-fallback"><h2>'+values['RECIPES']+'</h2>'+''.join(
        '<article><h3>'+html.escape(row['title'])+'</h3><p>'+html.escape(row['summary'])+'</p></article>' for row in visible)+'<a href="'+page_name(language,variant)+'">'+values['INSTALL']+'</a></section></noscript>'
    head = '<link rel="icon" href="assets/icon.svg"><meta name="description" content="'+values['DESCRIPTION']+'"><link rel="canonical" href="'+PUBLIC_BASE+canonical+'">'+schema
    if variant == 'kitchen':
        head += ''.join('<link rel="alternate" hreflang="'+lang+'" href="'+PUBLIC_BASE+target+'">' for lang,target in (('de','index.html'),('en','index-en.html')))
    page = page.replace('<html lang="de">', '<html lang="'+language+'">').replace('<body>', '<body class="public-book" data-public-language="'+language+'">')
    page = page.replace('</head>', head+'</head>').replace('</body>', fallback+'</body>')
    return page


def public_pages(site):
    legal = json.loads((ROOT / 'templates/legal.json').read_text())
    for language, sections in legal.items():
        suffix = '' if language == 'de' else '-en'
        for kind, content in sections.items():
            name = kind + suffix + '.html'
            other = kind + ('-en' if language == 'de' else '') + '.html'
            home = 'kitchen'+suffix+'.html'
            page = ('<!doctype html><html lang="'+language+'"><head><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light dark">'
                '<link rel="stylesheet" href="assets/site.css"><link rel="canonical" href="'+PUBLIC_BASE+name+'">'
                '<title>'+content['title']+' · Cookbook by Pengusto</title></head><body>'
                '<header class="site-header wrap"><a class="brand" href="'+home+'">Cookbook by Pengusto</a>'
                '<nav><a href="'+other+'">'+('English' if language=='de' else 'Deutsch')+'</a></nav></header>'
                '<main class="help-main wrap"><h1>'+content['title']+'</h1>'+content['body']+'</main>'
                '<footer class="wrap"><a href="'+home+'">Cookbook</a> · <a href="legal'+suffix+'.html">'
                +legal[language]['legal']['title']+'</a> · <a href="privacy'+suffix+'.html">'+legal[language]['privacy']['title']+'</a></footer></body></html>')
            (site / name).write_text(page)
    for name, variant, language in (
        ('index.html', 'kitchen', 'de'), ('index-en.html', 'kitchen', 'en'),
        ('kitchen.html', 'kitchen', 'de'), ('kitchen-en.html', 'kitchen', 'en'),
        ('cookbook.html', 'kitchen', 'de'), ('cookbook-plain.html', 'plain', 'de')):
        (site / name).write_text(public_book(variant, language))
    (site / '.nojekyll').write_text('')
    urls = ['index.html', 'index-en.html']+[page_name(lang,v) for lang in ('de','en') for v in VARIANTS]+['legal.html','legal-en.html','privacy.html','privacy-en.html','cookbook.html','cookbook-plain.html']
    (site / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+PUBLIC_BASE+name+'</loc></url>' for name in urls)+'</urlset>')
    # This file applies to a root-hosted export, not the /cookbook/ Pages path.
    (site / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+PUBLIC_BASE+'sitemap.xml\n')


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
        help_page = (ROOT / 'templates' / ('help.html' if language == 'de' else 'help-en.html')).read_text()
        help_page = help_page.replace('{{COUNT}}', str(len(rows))).replace('{{VERSION}}', json.loads((ROOT / 'bundle.json').read_text())['version'])
        (site / ('help.html' if language == 'de' else 'help-en.html')).write_text(help_page)
    (site / 'assets').mkdir(exist_ok=True)
    # Remove obsolete generated copies; preserve the original source images.
    for name in ('cookbook-hero.jpg', 'cookbook-hero-dark.jpg'):
        (site / 'assets' / name).unlink(missing_ok=True)
    for name in ('icon.svg', 'icon-dark.svg', 'site.css', 'cookbook-hero-transparent.png'):
        shutil.copyfile(ROOT / 'assets' / name, site / 'assets' / name)
    shutil.copytree(ROOT / 'assets/icons', site / 'assets/icons', dirs_exist_ok=True)
    shutil.copyfile(ROOT / 'LICENSE', site / 'LICENSE')
    public_pages(site)
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
    rows = catalog()
    for row in rows:
        package_files(row)
    print(f'OK: {len(rows)} canonical sources and reviewed runtime hashes; no external source dependency')


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
