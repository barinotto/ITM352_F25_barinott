import pandas as pd

url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

#using a try-except block to not have the system crash if there's an error
# useing my df = pd.read_csv() line, Im adding the extras that are being asked in the question in the lab.
try:
    df = pd.read_csv(
        url,
        dtype_backend="pyarrow",
        on_bad_lines="skip",
        engine="python"
    )
        #Converting the datatype if it's not already a pyarrow dtype.
    if any("pyarrow" not in str(dtype) for dtype in df.dtypes):
        df = df.convert_dtypes(dtype_backend="pyarrow")

    print("First 5 rows:")
    print(df.head(5))
    print("\nData types:")
    print(df.dtypes)

except Exception as e:
    print("Failed to load CSV:", e)
