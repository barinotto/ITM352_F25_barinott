import re

# Define a list of taxi trip durations in miles
trip_miles = [1.1, 0.8, 2.5, 2.6]

# Define a tuple of fares (originally strings with $)
trip_fares = ("$6.25", "$5.25", "$10.50", "$8.05")

# Convert fares to numbers using regex
numeric_fares = [float(re.sub(r'\$(.*)', r'\1', fare)) for fare in trip_fares]

# Create dictionary mapping miles -> numeric fares
trips = dict(zip(trip_miles, numeric_fares))

# Print dictionary
print(trips)

# Print the duration and cost of the 3rd trip (formatted with $ again for display)
third_miles = trip_miles[2]
third_fare = trips[third_miles]
print(f"3rd trip: {third_miles} miles, ${third_fare:.2f}")
