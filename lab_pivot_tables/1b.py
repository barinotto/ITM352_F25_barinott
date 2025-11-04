# Ben Barinotto
# 11-03-2025
# Lab: Pivot Tables

#import library again
import pandas as pd

#load the data
url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"
df = pd.read_csv(url)

#convert the order date colum into standard datetime format
df["order_date"]= pd.to_datetime(df["order_date"], errors="coerce")

#now checking first 5 rows and data types
print("First 5 rows after converting 'order_date':")
print(df.head(5))
print("\nData types after conversion:")
print(df.dtypes)
