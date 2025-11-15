"""3b.py
Fetch the Shidler ITM people page, parse with BeautifulSoup, locate the people entries,
build a list of person names and print them and the total count.
This script uses a few heuristics to find the people blocks on the page.
"""
import re
import requests
from bs4 import BeautifulSoup

URL = 'https://shidler.hawaii.edu/itm/people'


def extract_people(soup):
    # Try common patterns used by Drupal Views or profile pages
    people = []

    # 1) look for view rows (class containing 'views-row')
    rows = soup.find_all(class_=re.compile(r"views-row"))
    if rows:
        for r in rows:
            # look for a heading or link with the person's name
            name_tag = r.find(['h2', 'h3', 'h4', 'a'])
            if name_tag and name_tag.get_text(strip=True):
                people.append(name_tag.get_text(strip=True))
    # 2) fallback: look for anchor tags whose href contains '/itm/' or 'people' and has non-empty text
    if not people:
        anchors = soup.find_all('a', href=True)
        for a in anchors:
            href = a['href']
            text = a.get_text(strip=True)
            if text and ('/itm/' in href or '/people' in href or 'shidler.hawaii.edu/itm' in href):
                people.append(text)

    # 3) final fallback: try elements with class names that look like 'person', 'profile', 'staff'
    if not people:
        candidates = soup.find_all(class_=re.compile(r"person|profile|staff|people", re.I))
        for c in candidates:
            text = c.get_text(separator=' ', strip=True)
            if text:
                # split lines and pick lines that look like names (two words, title-case)
                for part in text.split('\n'):
                    part = part.strip()
                    if len(part.split()) in (2,3) and part[0].isupper():
                        people.append(part)

    # deduplicate while preserving order
    seen = set()
    names = []
    for p in people:
        if p not in seen:
            seen.add(p)
            names.append(p)
    return names


def main():
    resp = requests.get(URL, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'lxml')
    names = extract_people(soup)
    print(f'Found {len(names)} people:')
    for n in names:
        print('-', n)


if __name__ == '__main__':
    main()
