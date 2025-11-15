import requests
import pandas as pd

URL = (
    'https://data.cityofchicago.org/resource/97wa-y6ff.json'
    '?$select=driver_type,count(license)&$group=driver_type'
)


def main():
    resp = requests.get(URL, timeout=15)
    resp.raise_for_status()
    records = resp.json()
    df = pd.DataFrame.from_records(records)

    # find the count column (Socrata returns key like 'count_license')
    count_col = next((c for c in df.columns if c.lower().startswith('count')), None)
    if count_col is None or 'driver_type' not in df.columns:
        print('Unexpected JSON structure. Columns:', list(df.columns))
        return

    df = df.rename(columns={count_col: 'count'})
    # ensure order
    df = df[['count', 'driver_type']]

    # convert count to integer where possible
    try:
        df['count'] = df['count'].astype(int)
    except Exception:
        # keep as-is if conversion fails
        pass

    df = df.set_index('driver_type')
    print('DataFrame (index=driver_type):')
    print(df)


if __name__ == '__main__':
    main()
