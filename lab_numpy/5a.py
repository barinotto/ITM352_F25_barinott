import argparse
from pathlib import Path
import sys
import requests
import pandas as pd

DRIVE_FILE_ID = "1M-X_bypJJ6K5p6eM6aYBwt1qIizIiIex"
DOWNLOAD_URL = f"https://drive.google.com/uc?export=download&id={DRIVE_FILE_ID}"


def download_if_missing(url: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists():
        print(f"Using cached file: {out_path}")
        return
    print(f"Downloading {url} -> {out_path}")
    resp = requests.get(url)
    resp.raise_for_status()
    out_path.write_bytes(resp.content)


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", help="local path to save/download CSV", default="data/taxi.csv")
    args = parser.parse_args(argv[1:])

    out_path = Path(args.cache)
    try:
        download_if_missing(DOWNLOAD_URL, out_path)
    except Exception as e:
        print(f"Failed to download CSV: {e}")
        sys.exit(1)

    try:
        df = pd.read_csv(out_path)
    except Exception as e:
        print(f"Failed to read CSV into DataFrame: {e}")
        sys.exit(2)

    # Print dimensions and first 10 rows
    print(f"\nDataFrame shape: {df.shape}")
    print("\nFirst 10 rows:")
    print(df.head(10).to_string(index=False))


if __name__ == "__main__":
    main(sys.argv)
