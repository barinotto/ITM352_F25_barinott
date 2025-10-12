# append input to tuple in Exercise 3
# Name: Ben Barinotto
# Date: 10/11/2025

# Original tuple
data = ("hello", 10, "goodbye", 3, "goodnight", 5, "morning", "football", 7)

# Try to append (which will fail), then handle using unpacking
try:
    data.append(2)  # Tuples don't support append
except AttributeError:
    # Use unpacking to create a new tuple with the new value added
    data = (*data, 2)

# Continue the program and print the updated tuple
print("Updated tuple:", data)
