from pathlib import Path
import csv
import sys


def compute_taxi_stats(csv_path: Path):
	total_fare = 0.0
	count = 0
	max_miles = 0.0

	with csv_path.open('r', encoding='utf-8', newline='') as fh:
		reader = csv.DictReader(fh)
		for row in reader:
			# Trip Miles is header "Trip Miles", Fare is header "Fare"
			miles_str = (row.get('Trip Miles') or '').strip()
			fare_str = (row.get('Fare') or '').strip()

			try:
				miles = float(miles_str) if miles_str != '' else 0.0
			except Exception:
				miles = 0.0

			try:
				fare = float(fare_str) if fare_str != '' else 0.0
			except Exception:
				fare = 0.0

			total_fare += fare
			count += 1
			if miles > max_miles:
				max_miles = miles

	avg_fare = (total_fare / count) if count else 0.0
	return count, total_fare, avg_fare, max_miles


def main():
	# Accept an optional CSV path so the script works regardless of cwd.
	# If none provided, look for taxi_1000.csv next to this script.
	import argparse

	parser = argparse.ArgumentParser(description='Compute taxi stats from CSV')
	parser.add_argument('csv', nargs='?', help='path to taxi_1000.csv', default=None)
	args = parser.parse_args()

	if args.csv:
		csv_file = Path(args.csv)
	else:
		csv_file = Path(__file__).resolve().parent / 'taxi_1000.csv'

	if not csv_file.exists():
		print(f"ERROR: CSV not found at {csv_file.resolve()}", file=sys.stderr)
		sys.exit(2)

	rows, total, avg, max_miles = compute_taxi_stats(csv_file)
	print(f"rows_processed={rows}")
	print(f"total_fare={total:.2f}")
	print(f"average_fare={avg:.2f}")
	print(f"max_trip_miles={max_miles}")


if __name__ == '__main__':
	main()

