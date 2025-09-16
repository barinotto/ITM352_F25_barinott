# Have the user enter a decimal between 1 and 100
user_input = input("Please enter a float number between 1 and 100: ")

# Don't forget to convert the input (string) to an integer (float) 
number = float(user_input)

# Squaring the number
squared_number = number ** 2

# Print the result back to the user
print(f"You entered {number}, and the square of {number} is {squared_number}.")
