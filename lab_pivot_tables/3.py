# Ben Barinotto
# 11-03-2025
# Lab: Pivot Tables

#import once again
import pandas as pd
import numpy as np

# Load the data again
url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"
df = pd.read_csv(url)

# Convert numeric columns again
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

# Create sales column again
df["sales"] = df["quantity"] * df["unit_price"]

# Clean text columns as a good practice
df["sales_region"] = df["sales_region"].astype(str).str.strip().str.title()
df["order_type"] = df["order_type"].astype(str).str.strip().str.title()

# Create pivot table
pivot = pd.pivot_table(
    df,
    values="sales",
    index="sales_region",
    columns="order_type",
    aggfunc=[np.sum, np.mean],  # Sum and average sales
    margins=True,
    margins_name="Total",
    fill_value=0,
)

# Show all columns and format currency
pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", "${:,.2f}".format)

# Display result
print("\nPivot table: Total & Average Sales by Region and Order Type\n")
print(pivot)
