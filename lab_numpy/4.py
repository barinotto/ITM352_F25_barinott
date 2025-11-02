"""
Usage:
    python3 lab_numpy/4.py [--cache path/to/local.json]

If run without a cache path the script will download into ./data/taxi.json
and reuse it on subsequent runs.
"""
import argparse
import json
from pathlib import Path
import sys
import requests
import pandas as pd

DRIVE_FILE_ID = "1-MpDUIRZxhFnN-rcDdJQMe_mcCSciaus"
DOWNLOAD_URL = f"https://drive.google.com/uc?export=download&id={DRIVE_FILE_ID}"


def download_drive_file(url: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {url} -> {out_path}")
    resp = requests.get(url)
    resp.raise_for_status()
    out_path.write_bytes(resp.content)


def load_json_to_df(path: Path) -> pd.DataFrame:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    # If the JSON is a list of records, create DataFrame directly
    if isinstance(data, list):
        return pd.DataFrame(data)
    # If it's a dict with a top-level list under some key, try to find it
    for k, v in data.items() if isinstance(data, dict) else []:
        if isinstance(v, list):
            return pd.DataFrame(v)
    # Fallback: attempt to normalize JSON
    return pd.json_normalize(data)


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", help="local path to save/download JSON", default="data/taxi.json")
    args = parser.parse_args(argv[1:])

    out_path = Path(args.cache)
    if not out_path.exists():
        try:
            download_drive_file(DOWNLOAD_URL, out_path)
        except Exception as e:
            print(f"Failed to download file from Google Drive: {e}")
            sys.exit(1)

    try:
        df = load_json_to_df(out_path)
    except Exception as e:
        print(f"Failed to load JSON into DataFrame: {e}")
        sys.exit(2)

    # Print summary information
    print("\nDataFrame info:")
    print(df.info())

    print("\nDescriptive statistics (describe):")
    print(df.describe(include='all'))

    print("\nMedian for numeric columns:")
    try:
        print(df.median(numeric_only=True))
    except Exception as e:
        print(f"Failed to compute median: {e}")


if __name__ == "__main__":
    main(sys.argv)
