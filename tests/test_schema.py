"""JSON-LD must match the actual rendered catalog and remain safe in HTML."""
import html.parser
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('schema_builder', ROOT / 'scripts/cookbook.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class Page(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.scripts, self.cards = [], []
        self.script = None
        self.card = None
        self.field = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'script':
            self.script = {'type': attrs.get('type'), 'text': ''}
            self.scripts.append(self.script)
        if tag == 'article':
            self.card = {'title': '', 'summary': '', 'cooking_title': ''}
            self.cards.append(self.card)
        if self.card is not None:
            if tag == 'h2':
                self.field = 'title'
            elif tag == 'p' and attrs.get('class') == 'cooking-title':
                self.field = 'cooking_title'
            elif tag == 'p' and not attrs and not self.card['summary']:
                self.field = 'summary'

    def handle_data(self, text):
        if self.script is not None:
            self.script['text'] += text
        if self.card is not None and self.field is not None:
            self.card[self.field] += text

    def handle_endtag(self, tag):
        if tag == 'script':
            self.script = None
        if tag in ('h2', 'p'):
            self.field = None
        if tag == 'article':
            self.card = None


class SchemaContracts(unittest.TestCase):
    def test_jsonld_matches_visible_cards_without_unverified_claims(self):
        for language, variant, filename in ((lang, v, builder.page_name(lang, v)) for lang in ('de', 'en') for v in ('plain', 'kitchen')):
            with self.subTest(language=language, variant=variant):
                page = Page()
                page.feed((ROOT / 'site' / filename).read_text())
                self.assertEqual(len(page.scripts), 1)
                self.assertEqual(page.scripts[0]['type'], 'application/ld+json')
                data = json.loads(page.scripts[0]['text'])
                self.assertEqual(set(data), {'@context', '@type', 'name', 'inLanguage', 'mainEntity'})
                self.assertEqual(data['@context'], 'https://schema.org')
                self.assertEqual(data['@type'], 'CollectionPage')
                self.assertEqual(data['name'], 'Cookbook by Pengusto')
                self.assertEqual(data['inLanguage'], language)
                listing = data['mainEntity']
                self.assertEqual(listing['@type'], 'ItemList')
                self.assertEqual(listing['numberOfItems'], len(page.cards))
                self.assertEqual(len(listing['itemListElement']), len(page.cards))
                for position, (item, card) in enumerate(zip(listing['itemListElement'], page.cards), 1):
                    self.assertEqual(item, {'@type': 'ListItem', 'position': position,
                                           'item': {'@type': 'CreativeWork', 'name': card['title'],
                                                    'description': card['summary']}})
                self.assertEqual(len(page.cards), 8)
                self.assertEqual([i['item']['name'] for i in listing['itemListElement']],
                                 [row['title' if variant == 'plain' else 'cooking_title'] for row in builder.catalog()])
                self.assertEqual(page.scripts[0]['text'].count('https://'), 1)
                self.assertNotIn('http://', page.scripts[0]['text'])
                self.assertTrue(all('alternateName' not in i['item'] for i in listing['itemListElement']))

    def test_catalog_changes_are_reflected_and_cannot_escape_script(self):
        title = '</script><script>alert("demo")</script> & <Test>'
        summary = 'Neue Beschreibung mit Umlauten: äöü.'
        page = Page()
        page.feed(builder.schema_script([{'title': title, 'summary': summary}]))
        self.assertEqual(len(page.scripts), 1)
        self.assertEqual(page.scripts[0]['type'], 'application/ld+json')
        data = json.loads(page.scripts[0]['text'])
        self.assertEqual(data['mainEntity']['numberOfItems'], 1)
        item = data['mainEntity']['itemListElement'][0]['item']
        self.assertEqual(item['name'], title)
        self.assertEqual(item['description'], summary)
        self.assertNotIn('<', page.scripts[0]['text'])
