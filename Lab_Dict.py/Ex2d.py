#{{'key': 1.1, 'value': 6.25}', {'key': 0.8, 'value': 5.25}', {'key': 2.5, 'value': 10.50}', {'key': 2.6, 'value': 8.05}'}
# [
#{"miles":6.25, "fares": 1.1,}
#]
trips = [
    {'miles': 1.1, 'fare': 6.25},
    {'miles': 0.8, 'fare': 5.25},
    {'miles': 2.5, 'fare': 10.50},
    {'miles': 2.6, 'fare': 8.05}
]

print(f"The Third trip was {trips[2]['miles']} miles and cost ${trips[2]['fare']}")