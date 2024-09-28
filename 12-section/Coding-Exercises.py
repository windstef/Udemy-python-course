# Coding Exercise 2
# Your task for this exercise is to complete the strength function. The function is supposed to check the strength of the user's password.
# https://www.udemy.com/course/the-python-mega-course/learn/quiz/5902640#overview
#
#
# The function should:
#
# 1. get a password argument
#
# 2. return the string "Strong Password" if all of the following conditions are true:
#
# Eight or more characters
#
# At least one uppercase letter.
#
# At least one digit.
#
# 3. returns "Weak Password" if at least one of the three conditions is not met.
#
# Note:  You can make use of the code we developed in the Bonus Example on Day 9.

def strength(password):
    length = len(password) > 7
    print(length)

    upper_list = [i.isupper() for i in password]
    upper = True in upper_list
    print(upper)

    digit_list = [i.isdigit() for i in password]
    print(digit_list)
    digit = True in digit_list
    print(digit)

    if length & upper & digit:
        return "Strong Password"
    else:
        return "Weak Password"


print(strength("Hifsdf1Rt5"))


# Hints
# The function takes one parameter named password, which represents the password to be checked.
#
# Create an empty dictionary named result to store the strength attributes.
#
# Use an if statement to check the length of the password. Set the length attribute in the result dictionary accordingly.
#
# Initialize two boolean variables, digit and uppercase, as False.
#
# Use a for loop to iterate over each character in the password.
#
# Use isdigit() method to check if a character is a digit.
#
# Use isupper() method to check if a character is an uppercase letter.
#
# Set the values of digit and uppercase accordingly.
#
# Store the values of digit and uppercase in the result dictionary with corresponding keys.
#
# Use the all() function to check if all the values in the result dictionary are True.
#
# Return "Strong Password" if all values are True, otherwise return "Weak Password".

#####################################

# Solution
#
#
# # Define a function named strength that takes one parameter, password
# def strength(password):
#     # Create an empty dictionary to store the strength attributes
#     result = {}
#
#     # Check the length of the password
#     if len(password) >= 8:
#         result["length"] = True
#     else:
#         result["length"] = False
#
#     # Check if the password contains a digit and an uppercase letter
#     digit = False
#     uppercase = False
#
#     # Iterate over each character in the password
#     for i in password:
#         # Check if the character is a digit
#         if i.isdigit():
#             digit = True
#         # Check if the character is an uppercase letter
#         if i.isupper():
#             uppercase = True
#
#     # Store the results in the dictionary
#     result["digits"] = digit
#     result["upper-case"] = uppercase
#
#     # Check if all the strength attributes are True
#     if all(result.values()):
#         # Return "Strong Password" if all attributes are True
#         return "Strong Password"
#     else:
#         # Return "Weak Password" if any attribute is False
#         return "Weak Password"


##################################################
# Coding Exercise 3
# Define a function that takes a list as an argument and returns the average value of the list items. For example, if I called your function with foo([10, 20, 30, 40]) it should return 25, the average of the numbers of the list.

# def get_average(list_arg):
#     sumOfList = 0
#     for i in list_arg:
#         sumOfList = sumOfList + i
#
#     size = len(list_arg)
#
#     average = sumOfList / size
#     return average

# Hints


# Use the sum() function to calculate the sum of all elements in the list.
#
# Use the len() function to determine the length of the list.
#
# Divide the sum by the length of the list to calculate the average value.
#
# Return the calculated average value from the function.

# Solution
#
# def foo(mylist):
#     # Calculate the sum of all elements in the list and divide it by the length of the list
#     return sum(mylist) / len(mylist)


# Explanation
#
# The function foo takes a single parameter mylist, which is expected to be a list of numbers.
#
# Inside the function, it calculates the sum of all elements in the list using the sum() function.
#
# Then, it divides the sum by the length of the list using the len() function.
#
# The result is the average value of the numbers in the list.
#
# The function returns the calculated average value.
