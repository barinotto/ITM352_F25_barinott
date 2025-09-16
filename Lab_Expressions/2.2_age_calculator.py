# Ask the user to enter the year they were born
year_input = input("Enter the year you were born (4 digits): ")

# Convert the input (string) into an integer
birth_year = int(year_input)

# Current year (documention purposes)
current_year = 2025

# Calculate the age (we are documenting current_year rather than just putting in 2025 "randomly")
age = current_year - birth_year

# Print the result back to the user
print(f"You entered {birth_year}. Your calculated age in {current_year} is {age}.")
