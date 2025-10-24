try:
    with open("names.txt", "r") as file:
        names = [line.strip() for line in file.readlines()]
        print(names)
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: The file exists but is not readable.")
