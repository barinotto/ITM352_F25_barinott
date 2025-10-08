# iterate through numbers 1-10 and print the number if it is not equal to 5
# Loop entirely
# Ben Barinotto
# 10/2/2025

for i in range(1, 11):
    if i == 5:
        continue
    if i == 8:
        print("Reached 8, stopping loop")
        break
    print(i)