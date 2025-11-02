# Filter the properties with 500 or more units and print the first 10 rows
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


def main():
    csv_path = Path("data/taxi.csv")
    try:
        download_if_missing(DOWNLOAD_URL, csv_path)
    except Exception as e:
        print(f"Failed to ensure CSV exists: {e}")
        sys.exit(1)

    df = pd.read_csv(csv_path)

    # Ensure 'units' column exists and is numeric
    if 'units' not in df.columns:
        print("No 'units' column found in the DataFrame.")
        print(f"Columns present: {list(df.columns)}")
        sys.exit(2)

    # Convert units to numeric if needed (coerce errors to NaN)
    df['units'] = pd.to_numeric(df['units'], errors='coerce')

    # Filter rows with units >= 500
    filtered = df[df['units'] >= 500]

    # Drop unnecessary columns if present
    cols_to_drop = [c for c in ['id', 'block', 'lot', 'easement'] if c in filtered.columns]
    filtered = filtered.drop(columns=cols_to_drop)

    print(f"Selected rows with units >= 500: {len(filtered)}")
    print("First 10 rows:")
    # Print first 10 rows without index for readability
    if filtered.empty:
        print("No rows match the filter.")
    else:
        print(filtered.head(10).to_string(index=False))


if __name__ == '__main__':
    main()
