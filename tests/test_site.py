"""Contracts for the deployable website, independent of repository siblings."""
import html.parser
import json
from pathlib import Path
import unittest
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[1]


class Links(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids, self.head_links = [], set(), []
        self.in_head = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'head':
            self.in_head = True
        if tag == 'link' and self.in_head:
            self.head_links.append(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])

    def handle_endtag(self, tag):
        if tag == 'head':
            self.in_head = False


class WebsiteContracts(unittest.TestCase):
    def test_landing_discovery_preserves_language_and_naming_pairs(self):
        base_url = 'https://pengusto.github.io/cookbook/'
        for base in ('index', 'kitchen'):
            expected = {'de': base_url + base + '.html',
                        'en': base_url + base + '-en.html'}
            for language, url in expected.items():
                with self.subTest(language=language, variant=base):
                    parser = Links()
                    parser.feed((ROOT / 'site' / urlsplit(url).path.rsplit('/', 1)[1]).read_text())
                    alternates = [link for link in parser.head_links if link.get('rel') == 'alternate']
                    self.assertEqual(len(alternates), 2)
                    self.assertEqual({link['hreflang']: link['href'] for link in alternates}, expected)
                    self.assertEqual([link['href'] for link in parser.head_links if link.get('rel') == 'canonical'], [url])
                    self.assertIn('https://github.com/pengusto/cookbook', parser.links)

    def test_html_links_and_fragments_stay_inside_export(self):
        site = ROOT / 'site'
        for page in site.glob('*.html'):
            parser = Links()
            parser.feed(page.read_text())
            for link in parser.links:
                url = urlsplit(link)
                if url.scheme or url.netloc:
                    self.assertIn(url.scheme, ('https', 'data', 'mailto'))
                    continue
                target = (page.parent / unquote(url.path)).resolve() if url.path else page
                self.assertTrue(target.is_relative_to(site.resolve()), link)
                self.assertTrue(target.is_file(), link)
                if url.fragment and target.suffix == '.html':
                    destination = Links()
                    destination.feed(target.read_text())
                    self.assertIn(url.fragment, destination.ids, link)
            self.assertNotIn('noindex,nofollow', page.read_text())
            self.assertNotIn('htwelve', page.read_text())

    def test_website_archive_exactly_matches_site_without_private_state(self):
        site = ROOT / 'site'
        expected = {str(p.relative_to(site)): p.read_bytes() for p in site.rglob('*') if p.is_file()}
        rows = json.loads((ROOT / 'catalog.json').read_text())
        allowed = {'index.html', 'kitchen.html', 'help.html', 'LICENSE', 'assets/icon.svg', 'assets/icon-dark.svg', 'assets/cookbook-hero-transparent.png', 'assets/site.css', 'index-en.html', 'kitchen-en.html', 'help-en.html', 'downloads/SHA256SUMS'}
        allowed.update({'legal.html','legal-en.html','privacy.html','privacy-en.html','cookbook.html','cookbook-plain.html','robots.txt','sitemap.xml','.nojekyll'})
        allowed.update(f'assets/icons/{name}' for name in ('download.svg', 'book.svg', 'chef-hat.svg', 'message-circle.svg', 'arrow-right.svg', 'clipboard.svg', 'soup.svg', 'lock.svg', 'search.svg', 'bell.svg', 'list-details.svg', 'door-exit.svg', 'terminal-2.svg', 'LICENSE', 'LUCIDE-LICENSE', 'README.md'))
        allowed.update(f'downloads/cookbook-by-pengusto-{variant}-{host}.zip' for host in ('codex', 'claude') for variant in ('plain','kitchen'))
        for row in rows:
            if row['status'] == 'source':
                for variant in ('plain','kitchen'):
                    allowed.add(f'downloads/{variant}-{row["id"]}.zip')
                    allowed.update(f'skills/{variant}/{row["install_ids"][variant]}/{name}' for name in row['files'])
        self.assertEqual(set(expected), allowed, 'Unexpected or stale website export file')
        with zipfile.ZipFile(ROOT / 'dist/website.zip') as archive:
            self.assertEqual(set(archive.namelist()), set(expected))
            for name, data in expected.items():
                self.assertEqual(archive.read(name), data)
                self.assertFalse(any(p.startswith('.') for p in Path(name).parts) and name != '.nojekyll')
                self.assertNotIn('sources.local.json', name)
                self.assertNotIn(b'/Users/enisuysal/', data)
        self.assertIn('index.html', expected)
        self.assertIn('help.html', expected)
        self.assertIn('LICENSE', expected)
        self.assertIn('assets/icon.svg', expected)

    def test_language_and_naming_navigation_preserve_selection(self):
        for language in ('de', 'en'):
            for variant, base in (('plain', 'index'), ('kitchen', 'kitchen')):
                with self.subTest(language=language, variant=variant):
                    suffix = '' if language == 'de' else '-en'
                    page = (ROOT / 'site' / (base + suffix + '.html')).read_text()
                    self.assertIn(f'<html lang="{language}">', page)
                    self.assertIn('href="index' + suffix + '.html#skills"', page)
                    self.assertIn('href="kitchen' + suffix + '.html#skills"', page)
                    self.assertIn('href="' + base + '.html"', page)
                    self.assertIn('href="' + base + '-en.html"', page)
                    self.assertIn(f'cookbook-by-pengusto-{variant}-codex.zip', page)
                    self.assertIn(f'cookbook-by-pengusto-{variant}-claude.zip', page)
                    self.assertEqual(page.count('<article class="skill"'), len(json.loads((ROOT / 'catalog.json').read_text())))
                    self.assertNotIn('{{', page)
                    self.assertNotIn('npm install', page)


class PublicBetaContracts(unittest.TestCase):
    def test_dark_assets_match_system_preference_without_external_runtime(self):
        for name in ('index.html', 'kitchen.html', 'index-en.html', 'kitchen-en.html', 'help.html', 'help-en.html'):
            text = (ROOT / 'site' / name).read_text()
            self.assertIn('content="light dark"', text)
            self.assertIn('media="(prefers-color-scheme: dark)"', text)
            self.assertIn('assets/icon-dark.svg', text)
            if not name.startswith('help'):
                self.assertIn('assets/cookbook-hero-transparent.png', text)
                self.assertNotIn('cookbook-hero-dark.jpg', text)
                self.assertNotIn('cookbook-hero.jpg', text)
        css = (ROOT / 'site/assets/site.css').read_text()
        self.assertIn('@media(prefers-color-scheme:dark)', css)
        self.assertTrue((ROOT / 'site/assets/cookbook-hero-transparent.png').is_file())

    def test_hero_has_real_transparency_and_solid_foreground(self):
        import struct
        import zlib
        data = (ROOT / 'site/assets/cookbook-hero-transparent.png').read_bytes()
        self.assertEqual(data[:8], b'\x89PNG\r\n\x1a\n')
        width, height, depth, color, _, _, interlace = struct.unpack('>IIBBBBB', data[16:29])
        self.assertEqual((depth, color, interlace), (8, 6, 0))
        compressed, offset = bytearray(), 8
        while offset < len(data):
            size = int.from_bytes(data[offset:offset + 4], 'big')
            if data[offset + 4:offset + 8] == b'IDAT':
                compressed.extend(data[offset + 8:offset + 8 + size])
            offset += size + 12
        raw, stride = zlib.decompress(compressed), width * 4
        previous, transparent, opaque = bytearray(stride), 0, 0
        for y in range(height):
            start = y * (stride + 1)
            kind, row = raw[start], bytearray(raw[start + 1:start + 1 + stride])
            for x in range(stride):
                left, up, corner = (row[x - 4] if x >= 4 else 0), previous[x], (previous[x - 4] if x >= 4 else 0)
                estimate = left + up - corner
                paeth = min((left, up, corner), key=lambda value: abs(estimate - value))
                row[x] = (row[x] + (0, left, up, (left + up) // 2, paeth)[kind]) & 255
            transparent += row[3::4].count(0)
            opaque += sum(alpha >= 250 for alpha in row[3::4])
            previous = row
        self.assertGreater(transparent, width * height // 10)
        self.assertGreater(opaque, width * height // 3)

    def test_readme_translations_preserve_commands_and_local_links(self):
        import re
        english = ROOT / 'README.md'
        expected_commands = re.findall(r'```sh\n(.*?)```', english.read_text(), re.S)
        pages = [english] + sorted((ROOT / 'docs/readme').glob('README.*.md'))
        self.assertEqual(len(pages), 8)
        for page in pages:
            text = page.read_text()
            self.assertEqual(re.findall(r'```sh\n(.*?)```', text, re.S), expected_commands, page.name)
            for target in re.findall(r'\]\(([^)]+)\)', text):
                url = urlsplit(target)
                if url.scheme:
                    continue
                self.assertTrue((page.parent / url.path).resolve().is_file(), (page, target))
            for row in json.loads((ROOT / 'catalog.json').read_text()):
                self.assertIn(row['title'], text)
                self.assertIn(row['cooking_title'], text)
