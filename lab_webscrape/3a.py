import requests
from bs4 import BeautifulSoup

URL = 'https://shidler.hawaii.edu/itm/people'


def main():
    resp = requests.get(URL, timeout=15)
    resp.raise_for_status()
    html = resp.text
    soup = BeautifulSoup(html, 'lxml')

    # print the type of the object and the first few lines of prettified HTML
    print('Soup object type:', type(soup))
    pretty = soup.prettify()
    lines = pretty.splitlines()
    print('\nFirst 10 lines of prettified HTML:')
    for i, line in enumerate(lines[:10], 1):
        print(f"{i:02d}: {line}")


if __name__ == '__main__':
    main()
