# Ben Barinotto
# 10/23/2025

# Open the file and read its contents
with open("names.txt", "r") as file:
    data = file.read()

# Split the text into individual names (assuming one name per line)
names = data.splitlines()

# Print the names
print("Names:")
for name in names:
    print(name)

# Print the total count
print("\nTotal number of names:", len(names))