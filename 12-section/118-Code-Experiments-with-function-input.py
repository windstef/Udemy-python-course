# 118
# Code Experiments

# The first experiment is about, the difference between function calls and definitions.
# Tip: None is basically to represent a nothing.

def greet(message):
    new_message = message.capitalize()
    # print(new_message)
    return new_message      # It is important to return (no necessary)


user_entry = input("What greeting do you want? ")
greeting = greet(user_entry)
print(greeting)

# print(len(greeting))
# TypeError: object of type 'NoneType' has no len()