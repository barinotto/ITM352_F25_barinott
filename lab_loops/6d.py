# append input to tuple in Exercise 3
# Name: Ben Barinotto
# Date: 10/11/2025

# Original tuple
data = ("hello", 10, "goodbye", 3, "goodnight", 5, "morning", "football", 7)

# Try to append, but handle it properly when it fails
try:
    data.append(2)  # This will raise AttributeError
except AttributeError:
    # Instead of reporting the error, fix it by creating a new tuple
    data = data + (2,)  # This creates a new tuple with 2 added

# Continue program as normal
print("Updated tuple:", data)
