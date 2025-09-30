# Create a list with some values (you can change this to test)
my_list = [10, "hello", 3.14, True, None]

# Get the length of the list
length = len(my_list)

# Control logic
if length < 5:
    print("The list has fewer than 5 elements.")
elif 5 <= length <= 10:
    print("The list has between 5 and 10 elements (inclusive).")
else:
    print("The list has more than 10 elements.")