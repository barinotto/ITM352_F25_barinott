# Use_Module.py

#from HandyMath import max, min

# Get user input
#num1 = float(input("Enter the first number: "))
#num2 = float(input("Enter the second number: "))

# Use HandyMath functions
#mid = midpoint(num1, num2)
#sqrt = squareroot(num1)
#power_result = power(num1, num2)
#max_num = max(num1, num2)
#min_num = min(num1, num2)

# Output using f-strings
#print(f"The midpoint of {num1} and {num2} is: {mid}")
#print(f"The square root of {num1} is: {sqrt}")
#print(f"{num1} raised to the power of {num2} is: {power_result}")
#print(f"The larger of {num1} and {num2} is: {max_num}")
#print(f"The smaller of {num1} and {num2} is: {min_num}")

# Use_Module.py (Extra Credit)

from HandyMath import max, min, power, describe_function

# Get user input
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

# Test describe_function with min, max, and power
print(describe_function(x, y, max))
print(describe_function(x, y, min))
print(describe_function(x, y, power))
