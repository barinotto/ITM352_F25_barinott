import pandas as pd

# Given lists from lab
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

# Creating DataFrame
df = pd.DataFrame({
    "Age": ages,
    "Gender": gender
}, index=names)

# Calculating average age by gender and convert to DataFrame for clean display
avg_age_by_gender = df.groupby("Gender")["Age"].mean().to_frame()

# Rounding to 1 decimal place for better readability
avg_age_by_gender = avg_age_by_gender.round(1)

# Print clean table
print("Average Age by Gender:\n")
print(avg_age_by_gender)
