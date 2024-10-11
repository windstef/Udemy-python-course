# 146
# Coding Exercise 1
# Your task is to create a program that generates a random whole number. Here is how the program should behave:

# As you can see, the program first asks the user to enter a whole number. Then, once the user enters a number, the program asks the user again to enter another number.
# Then, the program returns a random number that falls between the two whole numbers. Here is another example:

# Enter the lower bound: 1
# Enter the upper bound: 10
# 7

# As you can see, the program first asks the user to enter a whole number. Then, once the user enters a number, the program asks the user again to enter another number.
# Then, the program returns a random number that falls between the two whole numbers.

# Note: To create this program, you might need to do some internet research or use the Python module index to find out what module and what function of that module you can use to generate random numbers.
# While it is easy for me to provide some clues here on what module you should use, searching for information and becoming familiar with programming community sites such as Stackoverflow is part of the programming skillset you should acquire.
# Thus, it is essential to practice such skills as well so you are independent after you finish the course.

# Python Module Index
# https://docs.python.org/3/py-modindex.html

# solution:
# https://pythonhow.com/coding/d15c1/

import random

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

dif = upper - lower

if dif > 0:
    random_num = random.randint(lower, upper)
    print(random_num)
else:
    print(f"You typed upper number, {upper} less or equal than the lower number {lower}")