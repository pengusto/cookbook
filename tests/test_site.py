"""Validate the static Pages artifact without dependencies."""
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'docs'

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.refs = []
        self.copies = []
        self.images = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, f"duplicate id: {a['id']}"
            self.ids.add(a['id'])
        for key in ('href', 'src'):
            if key in a:
                self.refs.append(a[key])
        if 'data-copy' in a:
            self.copies.append(a['data-copy'])
        if tag == 'img':
            self.images.append(a)

def main():
    pages = {}
    for path in SITE.glob('*.html'):
        page = Page()
        page.feed(path.read_text())
        pages[path.resolve()] = page
        assert 'name="viewport"' in path.read_text()
    for path, page in pages.items():
        for ref in page.refs:
            url = urlsplit(ref)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if target.is_dir():
                target /= 'index.html'
            assert target.is_relative_to(SITE.resolve()), ref
            assert target.exists(), f"broken local link: {path.name}: {ref}"
            if url.fragment:
                assert url.fragment in pages[target].ids, ref
        assert all(i in page.ids for i in page.copies)
        assert all(i.get('alt') and i.get('width') and i.get('height') for i in page.images)
    index = (SITE / 'index.html').read_text()
    assert 'legal.html' in index and 'privacy.html' in index
    readme = (ROOT / 'README.md').read_text()
    images = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', readme)
    assert images, 'README must include a preview image'
    for ref in images:
        target = (ROOT / ref).resolve()
        assert target.is_relative_to(ROOT) and target.is_file(), ref
    assert (SITE / 'assets/you-got-this-preview.webp').read_bytes() == (
        ROOT / 'output/portfolio-handoff/you-got-this-preview.webp'
    ).read_bytes(), 'website and handoff previews must match'
    assert 'FINITE LOOP' in (ROOT / 'output/portfolio-handoff/prompt.txt').read_text()
    script = (SITE / 'copy.js').read_text()
    assert 'clipboard.writeText' in script and 'catch' in script
    assert all(term not in script for term in ('fetch(', 'localStorage', 'document.cookie'))
    print('ok: site links, fragments, images, copy targets and privacy boundaries passed')

if __name__ == '__main__':
    main()
