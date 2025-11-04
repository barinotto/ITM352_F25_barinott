# Ben Barinotto
# Lab: Pivot Tables
# 11-03-2025

#import the pandas library
import pandas as pd

#making url variable to easily switch out for fun
url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"
df = pd.read_csv(url)

#to show the first 5 rows only of the dataframe
df.head(5)

#needs the print function since VS code doesn't automatically display dataframes
print(df.head(5))

#Need to show the data types as well
print("\nData Types of Each Column:")
print(df.dtypes)