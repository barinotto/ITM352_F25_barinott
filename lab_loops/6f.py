# append input to tuple in Exercise 3
# Name: Ben Barinotto
# Date: 10/11/2025

# Original tuple
data = ("hello", 10, "goodbye", 3, "goodnight", 5, "morning", "football", 7)

try:
    data.append(2)  # This will raise AttributeError
except AttributeError:
    # Step 1: Convert to list
    data_list = list(data)

    # Step 2: Append the new value
    data_list.append(2)

    # Step 3: Convert back to tuple
    data = tuple(data_list)

# Print updated tuple
print("Updated tuple:", data)
