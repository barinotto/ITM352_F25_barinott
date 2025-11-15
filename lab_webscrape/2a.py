# small helper to read the Treasury yield curve table and print columns
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import pandas as pd

url = 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202410'

try:
    tables = pd.read_html(url)
    print(f"Found {len(tables)} table(s) on the page")
    if len(tables) == 0:
        raise SystemExit('No tables found')
    df = tables[0]
    print('\nColumns:')
    print(list(df.columns))
    print('\nPreview:')
    print(df.head().to_string(index=False))
except Exception as e:
    print('Error reading tables:', repr(e))
    raise
