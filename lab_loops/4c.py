# Create a function for recent purcahses and test it
# Name: Ben Barinotto
# Date: 10/11/2025

def check_budget(purchases, budget):
    total_spent = sum(purchases)
    if total_spent > budget:
        return f"You spent ${total_spent:.2f}, which is over budget"
    else:
        return f"You spent ${total_spent:.2f}, which is within budget"


# Test cases
def run_tests():
    test_cases = [
        # (purchases, budget, expected_output)
        ([36.13, 23.87, 183.35, 22.93, 11.62], 50, "You spent $277.90, which is over budget"),
        ([10, 20, 15], 50, "You spent $45.00, which is within budget"),
        ([5, 5, 5], 15, "You spent $15.00, which is within budget"),
        ([100], 99.99, "You spent $100.00, which is over budget"),
        ([], 100, "You spent $0.00, which is within budget")
    ]

    for i, (purchases, budget, expected) in enumerate(test_cases, 1):
        result = check_budget(purchases, budget)
        assert result == expected, f"Test case {i} failed: expected '{expected}', got '{result}'"
        print(f"Test case {i} passed!")

# Run the tests
run_tests()