# append input to tuple in Exercise 3
# Name: Ben Barinotto
# Date: 10/11/2025

# Original tuple
data = ("hello", 10, "goodbye", 3, "goodnight", 5, "morning", "football", 7)

try:
    data.append(2)
except AttributeError as e:
    print(f"Error: {e}. Tuples are immutable and do not support appending.")
