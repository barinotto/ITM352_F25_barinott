# Check the number of strings in a tuple
# Name: Ben Barinotto
# Date: 9/30/2025

data = ("hello", 10, "goodbye", 3, "goodnight", 5, "morning", "football", 7)
string_count = 0

for item in data:
    if (type(item) == str): #chck if the item is a string
        string_count += 1
print(f"There are {string_count} strings in the tuple.")