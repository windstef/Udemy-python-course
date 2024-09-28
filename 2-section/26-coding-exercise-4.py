# Coding Exercise 4
# Create a program that prompts the user to input their name repeatedly. Then, the program repeatedly prints out the name with the first letter capitalized.
# Solution
# https://pythonhow.com/coding/d2c3/

user_prompt = "What is your name: "
# user_promt = "Quel est votre nom?"

while True:
    name = input(user_prompt)
    print(name.capitalize())
