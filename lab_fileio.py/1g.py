with open("names.txt", "a") as file:
    file.write("\nBarinotto, Ben")  # adding my name on a new line

# Now read and print the full contents to confirm
with open("names.txt", "r") as file:
    contents = file.read()
    print(contents)
