import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import pandas as pd

url = 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202410'


def main():
    try:
        tables = pd.read_html(url)
    except Exception as e:
        print('Error reading tables:', repr(e))
        return
    if not tables:
        print('No tables found on the page')
        return
    df = tables[0]
    target_col = '1 Mo'
    if target_col not in df.columns:
        print(f"Column '{target_col}' not found. Available columns: {list(df.columns)}")
        return

    # the iternate rows and print the 1 month rate
    for idx, row in df.iterrows():
        date = row.get('Date')
        rate = row.get(target_col)
        print(f"{date}: {rate}")


if __name__ == '__main__':
    main()
