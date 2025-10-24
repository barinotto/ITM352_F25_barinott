# Open the file and read line by line
with open("names.txt", "r") as file:
    names = []
    line = file.readline()
    
    while line:
        names.append(line.strip())  # remove \n
        line = file.readline()      # read the next line

# Print names and count
print("Names:")
for name in names:
    print(name)

print("\nTotal number of names:", len(names))
