#get first name, middle initial, and last name
first_name = input("Enter your first name: ")
middle_initial = input("Enter your middle initial: ")
last_name = input("Enter your last name: ")

#Ex2a concatenate the strings to form a full name
#full_name = first_name + " " + middle_initial + " " + last_name

#Ex2b using f-strings to format the full name instead
#full_name = f"{first_name} {middle_initial} {last_name}"

#Ex2c using the % operator to format the full name instead (the s after the percent means that it's expecting a str, not float))
#full_name = "%s %s %s" % (first_name, middle_initial, last_name)

#Ex2d now using the format() method to format the full name
#name_format = "{} {} {}"
#full_name = name_format.format(first_name, middle_initial, last_name)

#Ex3e join() method
#full_name = " ".join([first_name, middle_initial, last_name])

#Ex3f Unpacking the argument using format() method
name_parts = [first_name, middle_initial, last_name]
full_name = "{} {}. {}".format(*name_parts)

print("Full name:", full_name)