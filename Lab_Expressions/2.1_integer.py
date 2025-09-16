# Ask the user to enter a whole number between 1 and 100
user_input = input("Please enter a whole number between 1 and 100: ")

# Convert the input (string) to an integer
number = int(user_input)

# Square the number using the exponentiation operator (**)
squared_number = number ** 2

# Print the result back to the user
print(f"You entered {number}, and the square of {number} is {squared_number}.")
