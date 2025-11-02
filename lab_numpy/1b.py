import numpy as np

# Create the 2D array
data = np.array([
    [10, 14629],
    [20, 25600],
    [30, 37002],
    [40, 50000],
    [50, 63179],
    [60, 79542],
    [70, 100162],
    [80, 130000],
    [90, 184292]
])

# Print header
print("Percentile\tIncome")

# Loop through rows and print each pair
for row in data:
    print(f"{int(row[0])}\t\t{int(row[1])}")
