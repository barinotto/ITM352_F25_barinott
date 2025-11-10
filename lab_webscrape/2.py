# Ben Barinotto
# 11-06-2025

import urllib.request
daily_treasury_yield_curve_url = 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202410'
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
treasury_yield_curve_df = pd.read_html(daily_treasury_yield_curve_url)
print(treasury_yield_curve_df.columns())