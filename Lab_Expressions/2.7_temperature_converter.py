def temperature_converter(): 

    # Convert the input (string) to a float
    fahrenheit = float(fahrenheit)

    # Convert Fahrenheit to Celsius using the formula
    celsius = (fahrenheit - 32) * (5/9)

    # Print the result
    print("You entered", fahrenheit, "°F, which is equivalent to", celsius, "°C.")

# Ask the user to enter a temperature in Fahrenheit
fahrenheit = input("Enter a temperature in Fahrenheit: ")
temperature_converter()
