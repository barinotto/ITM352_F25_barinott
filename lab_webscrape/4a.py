from sodapy import Socrata
import pandas as pd

DATASET = 'rr23-ymwb'
DOMAIN = 'data.cityofchicago.org'
LIMIT = 500


def fetch_df(limit=LIMIT):
    client = Socrata(DOMAIN, None)
    results = client.get(DATASET, limit=limit)
    df = pd.DataFrame.from_records(results)
    return df


def main():
    df = fetch_df()
    print(f'Retrieved {len(df)} rows, {len(df.columns)} columns')
    print('\nColumns:')
    print(list(df.columns))
    print('\nPreview:')
    print(df.head().to_string(index=False))

if __name__ == '__main__':
    main()
