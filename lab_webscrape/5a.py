import requests
import json

URL = (
    'https://data.cityofchicago.org/resource/97wa-y6ff.json'
    '?$select=driver_type,count(license)&$group=driver_type'
)


def main():
    resp = requests.get(URL, timeout=15)
    resp.raise_for_status()
    records = resp.json()
    print('Type of response:', type(records))
    print('Number of records:', len(records))
    print('\nRecords (pretty JSON):')
    print(json.dumps(records, indent=2))


if __name__ == '__main__':
    main()
