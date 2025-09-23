# Define the data again
trip_miles = [1.1, 0.8, 2.5, 2.6]
trip_fares = ("$6.25", "$5.25", "$10.50", "$8.05")

# Use zip() to pair miles with fares, then create a dictionary
zipped_trips = zip(trip_miles, trip_fares)

trips_dict = dict(zipped_trips)

# Print the full dictionary
print("Trip dictionary:", trips_dict[trip_miles[2]])
