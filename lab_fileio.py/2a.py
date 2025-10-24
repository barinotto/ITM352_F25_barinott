import csv

# Open and read your CSV file
with open("my_custom_spreadsheet.csv", "r") as file:
    reader = csv.DictReader(file)
    
    salaries = [float(row["Annual_Salary"]) for row in reader]

# Calculate average, max, and min
average_salary = sum(salaries) / len(salaries)
max_salary = max(salaries)
min_salary = min(salaries)

# Print results
print(f"Average Annual Salary: ${average_salary:,.2f}")
print(f"Maximum Annual Salary: ${max_salary:,.2f}")
print(f"Minimum Annual Salary: ${min_salary:,.2f}")
