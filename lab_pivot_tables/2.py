#Ben Barinoto
#Lab: Pivot Tables
#11-03-2025 (standard date format lol)

#import numpy and pandas library once again
import pandas as pd
import numpy as np

# load the data again
url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"
df = pd.read_csv(url)

# making sure order_date is a real datetime format
df["order_date"] = pd.to_datetime(df["order_date"], format="%Y-%m-%d", errors="coerce")

# forcing quantity and unit_price to be numeric before computing sales
df["quantity"]   = pd.to_numeric(df["quantity"], errors="coerce")
df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

# creating the sales column (sales = quantity * unit_price)
df["sales"] = df["quantity"] * df["unit_price"]

# ensure all columns of wide tables are fully printed
pd.set_option("display.max_columns", None)

# create the actual pivot table:
#    - index: group by sales_region (rows)
#    - columns: split by order_type (Retail/Wholesale become columns)
#    - values: sum of sales
#    - aggfunc: use NumPy’s sum (as required), not Python’s built-in sum
#    - margins=True adds a totals row/column named "Total"
#    - fill_value=0 replaces NaN in the final table with 0 for readability
pivot = pd.pivot_table(
    df,
    values="sales",
    index="sales_region",
    columns="order_type",
    aggfunc=np.sum,
    margins=True,
    margins_name="Total",
    fill_value=0,
)

print(pivot)
