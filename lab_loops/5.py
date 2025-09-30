celebrities_tuple = ("Taylor Swift", "Lionel Messi", "Max Verstappen", "Keanu Reeves", "Angelina Joile")
ages_tuple = (34, 36, 26, 59, 49)

celebrities_list = []
ages_list = []

for celeb in celebrities_tuple:
    celebrities_list.append(celeb)
for age in ages_tuple:
    ages_list.append(age)

celebrities_dict = {
    "celebrities": celebrities_list,
    "ages": ages_list
}
print(celebrities_dict)