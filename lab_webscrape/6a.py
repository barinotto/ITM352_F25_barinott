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
    # return the largest table
    if tables:
        return max(tables, key=lambda x: len(x.get_text()))
    return None


def main():
    resp = requests.get(URL, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'lxml')
    table = find_rates_table(soup)
    if table is None:
        print('No table found on the page')
        return
    print('Found table. Printing rows:\n')
    for tr in table.find_all('tr'):
        text = ' | '.join([td.get_text(separator=' ', strip=True) for td in tr.find_all(['th','td'])])
        if text.strip():
            print(text)

if __name__ == '__main__':
    main()
