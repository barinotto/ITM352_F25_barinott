def calculator():
    print("Welcome to the Calculator!")
    
    while True:  # Loop to allow multiple calculations
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        try:
            operation = int(input("Enter the number corresponding to the operation (1-5): "))
            if operation == 5:
                print("Goodbye!")
                break  # Exit the loop and program
            if operation not in [1, 2, 3, 4]:
                print("Invalid operation. Please choose a number between 1 and 5.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if operation == 1:
                result = num1 + num2
                print(f"The result is: {result}")
            elif operation == 2:
                result = num1 - num2
                print(f"The result is: {result}")
            elif operation == 3:
                result = num1 * num2
                print(f"The result is: {result}")
            elif operation == 4:
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result is: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()