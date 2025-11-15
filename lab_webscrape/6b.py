import requests
from bs4 import BeautifulSoup

URL = 'https://www.hicentral.com/hawaii-mortgage-rates.php'


def find_rates_table(soup):
    tables = soup.find_all('table')
    for t in tables:
        thead = t.find('thead')
        header_text = ''
        if thead:
            header_text = thead.get_text(separator=' ').lower()
        else:
            header_text = t.get_text(separator=' ').lower()
        if 'bank' in header_text or '30-year' in header_text or 'institution' in header_text or 'current' in header_text:
            return t
    if tables:
        return max(tables, key=lambda x: len(x.get_text()))
    return None


def parse_row(tr):
    cells = tr.find_all(['th','td'])
    texts = [c.get_text(separator=' ', strip=True) for c in cells]
    return texts


def main():
    resp = requests.get(URL, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'lxml')
    table = find_rates_table(soup)
    if table is None:
        print('No table found on the page')
        return

    # determining header columns
    headers = []
    thead = table.find('thead')
    if thead:
        headers = [th.get_text(separator=' ', strip=True) for th in thead.find_all('th')]
    else:
        # take first row as header if it has
        first_row = table.find('tr')
        if first_row:
            headers = [c.get_text(separator=' ', strip=True) for c in first_row.find_all(['th','td'])]

    print('Detected headers:', headers)

    # Iterate data rows
    rows = table.find_all('tr')
    start = 1 if headers and rows and (rows[0].find_all(['th','td']) and [c.get_text().strip() for c in rows[0].find_all(['th','td'])] == headers) else 0
    for tr in rows[start:]:
        cols = parse_row(tr)
        if not cols:
            continue
        # bank name + rates
        bank = cols[0]
        rates = cols[1:]
        print(bank + ': ' + ' | '.join(rates))

if __name__ == '__main__':
    main()
