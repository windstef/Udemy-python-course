# In today's bonus example, we are going to write a program
# which checks the strength of a password.
# The program will behave like this.

# So in the command line the program asks the user to enter a password.
# So let's say we enter hello456, and a capital H.
# You press enter, you get this output, "Strong Password."
# So the program checked this password and it returned "Strong Password."

# [command line]
# >>> Enter new password: hello456H
# Strong Password
#
# [/command line]

# So this was a strong password because it fulfilled three conditions.
# First it was eight characters or longer.
# The second condition was that the password contains at least one digit.
# And the third condition is it contains at least one uppercase letter.

# If one of these conditions wouldn't be true we would get here "Weak Password."


password = input("Enter new password: ")

# result = []
result = {}


# First condition: password has eight characters or longer.

if len(password) >= 8:
    # result.append(True)       # list
    result["length"] = True     # dict
else:
    # result.append(False)       # list
    result["length"] =False     # dict


# Second condition: password contains at least one digit.

digit = False

for i in password:
    if i.isdigit():
        digit = True    # list

# result.append(digit)        # list
result["digits"] = digit     # dict


# Third condition: password contains at least one uppercase letter.
uppercase = False

for i in password:
    if i.isupper():
        uppercase = True

# result.append(uppercase)        # list
result["upper-case"] = uppercase     # dict


# Display: "Strong Password" or "Weak Password"

print(result)       # list / dict
print(result.values())  # dict

# The all() function returns True
# when all the items of the list are True Booleans.
# >>> help(all)
# all(iterable, /)
#     Return True if bool(x) is True for all values x in the iterable.
#     If the iterable is empty, return True.

# print(all(result))  # list
print(all(result.values()))     # dict

# list / dict
# if all(result):   # list
if all(result.values()):    # dict
    print("Strong Password")
else:
    print("Weak Password")



################################################

## Improvement: Use of dictionary instead of a list

# >> dir(dict)

# example:

# list:
# a = [14, 20, 30]

# dictionary (key, value)
# b = {"height":14, "width":20, "depth":30}
