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
    df.columns = [c.strip() if isinstance(c, str) else c for c in df.columns]

    obj_cols = df.select_dtypes(include=['object']).columns.tolist()
    for c in obj_cols:
        df[c] = df[c].astype(str).str.strip()
        df[c] = df[c].replace({'-': '', '': ''})

    numeric_candidates = ['id', 'block', 'lot', 'units', 'land_sqft', 'gross_sqft', 'year_built', 'sale_price']
    for c in numeric_candidates:
        if c in df.columns:
            cleaned = df[c].astype(str).str.replace(r"[^0-9.\-]", "", regex=True)
            df[c] = pd.to_numeric(cleaned, errors='coerce')

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

    # Filter properties with units >= 500
    if 'units' in cleaned.columns:
        filtered = cleaned[cleaned['units'].fillna(-1) >= 500]
    else:
        filtered = cleaned.iloc[0:0]

    # Take the first 10 matching rows
    subset = filtered.head(10)

    # Drop rows with any nulls and remove duplicate rows
    subset_clean = subset.dropna().drop_duplicates()

    # Print the cleaned dtypes for the subset, then the rows
    print(subset_clean.dtypes)
    if not subset_clean.empty:
        print(subset_clean.to_string(index=False))


if __name__ == '__main__':
    main()
