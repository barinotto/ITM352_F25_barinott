import random

def generate_numbers(a_student_id, num_reqs):
    # Check that there are at least two requirements available to assign
    if num_reqs < 2:
        raise ValueError("Invalid number of requirements. Must have at least 2.")
    
    # Remove any dashes or spaces from the student_id
    id = ''.join(filter(str.isdigit, a_student_id))
    
    # Ensure the student_id is valid (8 digits)
    if len(id) != 8:
        raise ValueError("Invalid student ID. It should be 8 digits.")

    # --- Algorithmic Logic to Generate two numbers ---
    
    # Generate the first number using the sum of digits
    sum_digits = sum(int(digit) for digit in id)
    # Modulo arithmetic is used to keep the number in the range [1, num_reqs]
    first_num = (sum_digits % num_reqs) + 1

    # Generate the second number using the product of digits
    product_digits = 1
    for digit in id:
        if int(digit) != 0:
            product_digits *= int(digit)
    second_num = (product_digits % num_reqs) + 1

    # --- Fix for Uniqueness Logic ---
    # Ensure the numbers are different by cycling to the next available number.
    # This prevents an infinite loop and guarantees a unique number in the range [1, num_reqs].
    while second_num == first_num:
        # If second_num is the highest requirement number, wrap it to 1; otherwise, increment.
        if second_num == num_reqs:
            second_num = 1
        else:
            second_num += 1

    return first_num, second_num

# --- Example usage (FIXED) ---

# Define the total number of requirements available (e.g., 10)
MAX_REQUIREMENTS = 10 

try:
    student_id = input("Enter your student id (XXX-XX-XXX): ")
    
    # CORRECTED FUNCTION CALL: Passing both student_id and MAX_REQUIREMENTS
    num1, num2 = generate_numbers(student_id, MAX_REQUIREMENTS)
    
    print(f"Your two unique assigned requirements are: {num1} and {num2} (out of {MAX_REQUIREMENTS})")
    
except ValueError as e:
    print(f"Error: {e}")