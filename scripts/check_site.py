#!/usr/bin/env python3
"""Check a Jekyll build's internal URLs and Persian/English page parity.

Usage: python3 scripts/check_site.py [_site] [baseurl]
Uses only the Python standard library.
"""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.lang = None
        self.direction = None
        self.headings = 0
        self.main_count = 0
        self.main_depth = 0
        self.main_text = []
        self.switch = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'html':
            self.lang, self.direction = attrs.get('lang'), attrs.get('dir')
        if tag == 'h1':
            self.headings += 1
        if tag == 'main':
            self.main_count += 1
            self.main_depth += 1
        if tag in ('a', 'link', 'use') and 'href' in attrs:
            self.links.append(attrs['href'])
        if tag in ('img', 'script') and 'src' in attrs:
            self.links.append(attrs['src'])
        if tag in ('img', 'source') and 'srcset' in attrs:
            self.links.extend(candidate.strip().split()[0]
                              for candidate in attrs['srcset'].split(',')
                              if candidate.strip())
        if 'language-link' in attrs.get('class', '').split():
            self.switch = attrs.get('href')

    def handle_endtag(self, tag):
        if tag == 'main':
            self.main_depth -= 1

    def handle_data(self, data):
        if self.main_depth:
            self.main_text.append(data)


def check(output, baseurl):
    pages = {p: Page(p.read_text()) for p in output.rglob('*.html')}
    errors = []
    count = 0
    for path, page in pages.items():
        relative = path.relative_to(output).as_posix()
        url = baseurl + '/' + relative.removesuffix('index.html')
        en = relative.startswith('en/')
        expected_lang, expected_dir = ('en', 'ltr') if en else ('fa', 'rtl')
        if (page.lang, page.direction) != (expected_lang, expected_dir):
            errors.append(f'{relative}: wrong language or text direction')
        if page.headings != 1 or page.main_count != 1:
            errors.append(f'{relative}: expected one h1 and one main landmark')
        if any(n > 1 for n in Counter(page.ids).values()):
            errors.append(f'{relative}: duplicate HTML IDs')
        counterpart = relative.removeprefix('en/') if en else 'en/' + relative
        expected_switch = baseurl + '/' + counterpart.removesuffix('index.html')
        if page.switch != expected_switch or output / counterpart not in pages:
            errors.append(f'{relative}: missing or incorrect translation link')
        if en and re.search(r'[\u0600-\u06ff]', ''.join(page.main_text)):
            errors.append(f'{relative}: untranslated Persian text in English main content')
        if re.search(r'\{[{%]', path.read_text()):
            errors.append(f'{relative}: unrendered Liquid')
        for link in page.links:
            parsed = urlsplit(urljoin(url, link))
            if parsed.scheme or parsed.netloc:
                continue
            count += 1
            target_url = unquote(parsed.path)
            if baseurl and not target_url.startswith(baseurl + '/'):
                errors.append(f'{relative}: URL escapes baseurl: {link}')
                continue
            target = output / target_url[len(baseurl):].lstrip('/')
            if target.is_dir():
                target /= 'index.html'
            if not target.is_file():
                errors.append(f'{relative}: missing destination {link}')
            elif parsed.fragment:
                if target in pages:
                    ids = pages[target].ids
                elif target.suffix == '.svg':
                    ids = re.findall(r'\bid="([^"]+)"', target.read_text())
                else:
                    continue
                if unquote(parsed.fragment) not in ids:
                    errors.append(f'{relative}: missing fragment {link}')
    if not pages:
        errors.append('No generated HTML pages found; build Jekyll first.')
    # Check the data contracts used by the shared bilingual homepage.
    source = Path(__file__).resolve().parents[1]
    translations = json.loads((source / '_data/translations.json').read_text())
    if translations['fa'].keys() != translations['en'].keys():
        errors.append('Homepage translation keys differ between languages')
    for group in json.loads((source / '_data/design.json').read_text()).values():
        for item in group:
            for field in ('description', 'heading'):
                if field in item and set(item[field]) != {'fa', 'en'}:
                    errors.append(f'Missing translation in {item}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'PASS: {len(pages)} pages, {count} internal links, language counterparts and bilingual data.')
    return 0


if __name__ == '__main__':
    sys.exit(check(Path(sys.argv[1] if len(sys.argv) > 1 else '_site'),
                   sys.argv[2].rstrip('/') if len(sys.argv) > 2 else ''))
