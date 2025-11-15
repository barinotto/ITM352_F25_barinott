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
    # normalize columns we'll use
    df_columns = df.columns
    # choose identifier: prefer public_vehicle_number, fallback to record_id
    id_col = 'public_vehicle_number' if 'public_vehicle_number' in df_columns else 'record_id'
    make = 'vehicle_make' if 'vehicle_make' in df_columns else None
    model = 'vehicle_model' if 'vehicle_model' in df_columns else None
    fuel = 'vehicle_fuel_source' if 'vehicle_fuel_source' in df_columns else None

    for _, row in df.iterrows():
        ident = row.get(id_col, '')
        parts = []
        if make:
            m = row.get(make)
            if m:
                parts.append(str(m))
        if model:
            mo = row.get(model)
            if mo:
                parts.append(str(mo))
        name = ' '.join(parts) if parts else ('vehicle_'+str(ident))
        fuel_val = row.get(fuel, 'UNKNOWN') if fuel else 'UNKNOWN'
        print(f"{ident}: {name} -> {fuel_val}")

if __name__ == '__main__':
    main()
