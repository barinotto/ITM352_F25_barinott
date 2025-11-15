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
    if 'vehicle_fuel_source' not in df.columns:
        print("No 'vehicle_fuel_source' column found. Columns:", list(df.columns))
        return
    counts = df['vehicle_fuel_source'].fillna('UNKNOWN').value_counts()
    print('Counts per fuel source:')
    for fuel, cnt in counts.items():
        print(f"{fuel}: {cnt}")

if __name__ == '__main__':
    main()
