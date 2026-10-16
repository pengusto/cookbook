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
        self.links, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])


class WebsiteContracts(unittest.TestCase):
    def test_html_links_and_fragments_stay_inside_export(self):
        site = ROOT / 'site'
        for page in site.glob('*.html'):
            parser = Links()
            parser.feed(page.read_text())
            for link in parser.links:
                url = urlsplit(link)
                if url.scheme or url.netloc:
                    self.assertIn(url.scheme, ('https', 'data'))
                    continue
                target = (page.parent / unquote(url.path)).resolve() if url.path else page
                self.assertTrue(target.is_relative_to(site.resolve()), link)
                self.assertTrue(target.is_file(), link)
                if url.fragment and target.suffix == '.html':
                    destination = Links()
                    destination.feed(target.read_text())
                    self.assertIn(url.fragment, destination.ids, link)
            self.assertIn('noindex,nofollow', page.read_text())

    def test_website_archive_exactly_matches_site_without_private_state(self):
        site = ROOT / 'site'
        expected = {str(p.relative_to(site)): p.read_bytes() for p in site.rglob('*') if p.is_file()}
        rows = json.loads((ROOT / 'catalog.json').read_text())
        allowed = {'index.html', 'help.html', 'LICENSE', 'assets/icon.svg', 'downloads/SHA256SUMS'}
        allowed.update(f'downloads/vibe-coding-cookbook-{host}.zip' for host in ('codex', 'claude'))
        for row in rows:
            if row['status'] == 'snapshot':
                allowed.add(f'downloads/{row["id"]}.zip')
                allowed.update(f'skills/{row["id"]}/{name}' for name in row['files'])
        self.assertEqual(set(expected), allowed, 'Unexpected or stale website export file')
        with zipfile.ZipFile(ROOT / 'dist/website.zip') as archive:
            self.assertEqual(set(archive.namelist()), set(expected))
            for name, data in expected.items():
                self.assertEqual(archive.read(name), data)
                self.assertFalse(any(p.startswith('.') for p in Path(name).parts))
                self.assertNotIn('sources.local.json', name)
                self.assertNotIn(b'/Users/enisuysal/', data)
        self.assertIn('index.html', expected)
        self.assertIn('help.html', expected)
        self.assertIn('LICENSE', expected)
        self.assertIn('assets/icon.svg', expected)
