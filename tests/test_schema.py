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
    def __init__(self, title_tags=('h2',)):
        super().__init__()
        self.title_tags = title_tags
        self.html_language = None
        self.recipe_links = []
        self.recipe_link = None
        self.scripts, self.cards = [], []
        self.script = None
        self.card = None
        self.field = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.html_language = attrs.get('lang')
        if tag == 'a' and 'recipe-tab' in attrs.get('class', '').split():
            self.recipe_link = {'href': attrs.get('href'), 'name': ''}
            self.recipe_links.append(self.recipe_link)
        if tag == 'script':
            self.script = {'type': attrs.get('type'), 'text': ''}
            self.scripts.append(self.script)
        if tag == 'article':
            self.card = {'title': '', 'summary': '', 'cooking_title': ''}
            self.cards.append(self.card)
        if self.card is not None:
            if tag in self.title_tags:
                self.field = 'title'
            elif tag == 'p' and attrs.get('class') == 'cooking-title':
                self.field = 'cooking_title'
            elif tag == 'p' and not attrs and not self.card['summary']:
                self.field = 'summary'

    def handle_data(self, text):
        if self.recipe_link is not None:
            self.recipe_link['name'] += text
        if self.script is not None:
            self.script['text'] += text
        if self.card is not None and self.field is not None:
            self.card[self.field] += text

    def handle_endtag(self, tag):
        if tag == 'a':
            self.recipe_link = None
        if tag == 'script':
            self.script = None
        if tag in (*self.title_tags, 'p'):
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
                self.assertEqual(len(page.cards), len(builder.catalog()))
                self.assertEqual([i['item']['name'] for i in listing['itemListElement']],
                                 [row['title' if variant == 'plain' else 'cooking_title'] for row in builder.catalog()])
                self.assertEqual(page.scripts[0]['text'].count('https://'), 1)
                self.assertNotIn('http://', page.scripts[0]['text'])
                self.assertTrue(all('alternateName' not in i['item'] for i in listing['itemListElement']))

    def test_public_book_schema_matches_navigable_recipes_and_fallback(self):
        rows = builder.catalog()
        locales = json.loads((ROOT / 'ui/locales.json').read_text())
        routes = (
            ('index.html', 'kitchen', 'de'), ('index-en.html', 'kitchen', 'en'),
            ('kitchen.html', 'kitchen', 'de'), ('kitchen-en.html', 'kitchen', 'en'),
            ('cookbook.html', 'kitchen', 'de'), ('cookbook-plain.html', 'plain', 'de'))
        for filename, variant, language in routes:
            with self.subTest(filename=filename, variant=variant, language=language):
                page = Page(title_tags=('h3',))
                page.feed((ROOT / 'site' / filename).read_text())
                schema = [script for script in page.scripts if script['type'] == 'application/ld+json']
                self.assertEqual(len(schema), 1)
                data = json.loads(schema[0]['text'])
                self.assertEqual(set(data), {'@context', '@type', 'name', 'inLanguage', 'mainEntity'})
                self.assertEqual(data['@context'], 'https://schema.org')
                self.assertEqual(data['@type'], 'CollectionPage')
                self.assertEqual(data['name'], 'Cookbook by Pengusto')
                self.assertEqual(data['inLanguage'], language)
                self.assertEqual(page.html_language, language)
                summaries = locales[language]['summaries'].split('|')
                self.assertEqual(len(summaries), len(rows))
                expected = [
                    {'@type': 'ListItem', 'position': position,
                     'item': {'@type': 'CreativeWork',
                              'name': row['title' if variant == 'plain' else 'cooking_title'],
                              'description': summary}}
                    for position, (row, summary) in enumerate(zip(rows, summaries), 1)]
                self.assertEqual(data['mainEntity'], {
                    '@type': 'ItemList', 'numberOfItems': len(rows), 'itemListElement': expected})
                self.assertEqual(page.recipe_links, [
                    {'href': '#' + row['install_ids'][variant], 'name': item['item']['name']}
                    for row, item in zip(rows, expected)])
                self.assertEqual(page.cards, [
                    {'title': item['item']['name'], 'summary': item['item']['description'], 'cooking_title': ''}
                    for item in expected])
                self.assertNotIn('"@type": "Recipe"', schema[0]['text'])
                self.assertNotIn('aggregateRating', schema[0]['text'])
                self.assertNotIn('offers', schema[0]['text'])

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
