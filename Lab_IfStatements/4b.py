# Store your birth year in a variable
my_birth_year = 2005  # replace with your actual birth year

# Check leap year conditions
if (my_birth_year % 4 == 0 and my_birth_year % 100 != 0) or (my_birth_year % 400 == 0):
    print(f"{my_birth_year} is a Leap year")
else:
    print(f"{my_birth_year} is Not a leap year")
