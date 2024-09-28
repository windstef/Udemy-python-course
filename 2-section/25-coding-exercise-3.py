# Coding Exercise 2
# Create a program that prompts the user to input their name once. Then, the program repeatedly prints out the name with the first letter capitalized.
# Solution
# https://pythonhow.com/coding/d2c2/

user_prompt = "Enter your name: "

name = input(user_prompt)

while True:
    print(name.capitalize())
