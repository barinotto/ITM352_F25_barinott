# Open the file and read all lines at once into a list
with open("names.txt", "r") as file:
    names = [line.strip() for line in file.readlines()]

# Print the names and total count
print("Names:")
for name in names:
    print(name)

print("\nTotal number of names:", len(names))
