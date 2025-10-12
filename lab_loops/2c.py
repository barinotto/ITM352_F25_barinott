#create a list of even numbers from 2-50 (inclusive)
# Name: Ben Barinotto
# Date: 9/30/2025

evens = [2] # initialize list with 2

while evens[-1] <= 50: # continue until the last element is 50 or more
      evens.append(evens[-1] + 2) # append the next even number

print(evens)