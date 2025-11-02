from pathlib import Path
import sys
import pandas as pd
import requests

DRIVE_FILE_ID = "1M-X_bypJJ6K5p6eM6aYBwt1qIizIiIex"
DOWNLOAD_URL = f"https://drive.google.com/uc?export=download&id={DRIVE_FILE_ID}"


def download_if_missing(url: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists():
        return
    resp = requests.get(url)
    resp.raise_for_status()
    out_path.write_bytes(resp.content)


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # normalize column names
    df.columns = [c.strip() if isinstance(c, str) else c for c in df.columns]

    # strip whitespace for object columns and normalize known placeholders
    obj_cols = df.select_dtypes(include=['object']).columns.tolist()
    for c in obj_cols:
        df[c] = df[c].astype(str).str.strip()
        df[c] = df[c].replace({'-': '', '': ''})

    # coerce numeric candidates including sale_price
    numeric_candidates = ['id', 'block', 'lot', 'units', 'land_sqft', 'gross_sqft', 'year_built', 'sale_price']
    for c in numeric_candidates:
        if c in df.columns:
            cleaned = df[c].astype(str).str.replace(r"[^0-9.\-]", "", regex=True)
            df[c] = pd.to_numeric(cleaned, errors='coerce')

    # borough to nullable int if numeric
    if 'borough' in df.columns:
        borough_clean = df['borough'].astype(str).str.strip()
        if borough_clean.str.match(r'^\d+$').all():
            df['borough'] = pd.to_numeric(borough_clean, errors='coerce').astype('Int64')

    return df


def main():
    csv_path = Path('data/taxi.csv')
    try:
        download_if_missing(DOWNLOAD_URL, csv_path)
    except Exception as e:
        print(f"Failed to ensure CSV present: {e}")
        sys.exit(1)

    df = pd.read_csv(csv_path, dtype=str)
    cleaned = clean_dataframe(df)

    if 'sale_price' not in cleaned.columns:
        print("No 'sale_price' column found in data.")
        sys.exit(1)

    # Filter out zero sales (keep rows where sale_price is not 0 and not NaN)
    filtered = cleaned[cleaned['sale_price'].notna() & (cleaned['sale_price'] != 0)]

    # Take only the first 10 rows from the filtered set
    top10 = filtered.head(10)

    if top10.empty:
        print("No non-zero sales found after cleaning (or no rows available to show).")
    else:
        # Print only the first 10 rows
        print(top10.to_string(index=False))

        # compute and display average sale price of these 10 rows only
        avg = top10['sale_price'].mean()
        print(f"\nAverage sale_price (first 10 non-zero rows): {avg:.2f}")


if __name__ == '__main__':
    main()
