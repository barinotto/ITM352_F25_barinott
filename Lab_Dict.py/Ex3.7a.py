# Define a list of taxi trip durations in miles
trip_miles = [1.1, 0.8, 2.5, 2.6]

# Define a tuple of fares for the same number of trips
trip_fares = ("$6.25", "$5.25", "$10.50", "$8.05")

# Store both in a dictionary
trips = {
    "miles": trip_miles,
    "fares": trip_fares
}

# Print the dictionary
print(trips)

#ExB
print(trips['fares'][2])