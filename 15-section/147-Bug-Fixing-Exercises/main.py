from parsers import parse
import random

# Ask the user to enter a lower and an upper bound divided by a comma
user_input = input("Enter a lower bound and an upper bound divided a comma (e.g., 2,10)")

# Parse the user string by calling the parse function
parsed = parse(user_input)

# Pick a random int between the two numbers
rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])

print(rand)


# Error

# Traceback (most recent call last):
#   File "/home/stefkour/PycharmProjects/app1/pythonProject/15-section/147-Bug-Fixing-Exercises/main.py", line 8, in <module>
#     parsed = parse(user_input)
#              ^^^^^^^^^^^^^^^^^
#   File "/home/stefkour/PycharmProjects/app1/pythonProject/15-section/147-Bug-Fixing-Exercises/parsers.py", line 9, in parse
#     lower_bound = float(parts[0])
#                   ^^^^^^^^^^^^^^^
# ValueError: could not convert string to float: '3,12'


# https://www.udemy.com/course/the-python-mega-course/learn/lecture/32562272#overview


# Day 15, Bug Fixing Exercise 1
# https://pythonhow.com/coding/d15b1/

