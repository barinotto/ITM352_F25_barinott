# Test cases: list of lists
test_cases = [
    [1, 2, 3],                   # fewer than 5 elements
    [10, "a", 3.14, True, None], # exactly 5 elements
    list(range(10)),              # exactly 10 elements
    list(range(12))               # more than 10 elements
]

# Loop through test cases
for case in test_cases:
    length = len(case)
    print(f"Testing list (length {length}): {case}")

    if length < 5:
        print("Result: The list has fewer than 5 elements.\n")
    elif 5 <= length <= 10:
        print("Result: The list has between 5 and 10 elements (inclusive).\n")
    else:
        print("Result: The list has more than 10 elements.\n")
