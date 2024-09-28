# 109
# Code Experiments

# The first experiment is about, the difference between function calls and definitions.
# Tip: None is basically to represent a nothing.

def greet():
    message = "hello"
    new_message = message.capitalize()
    print("hey from function")
    # print(new_message)
    # return new_message      # It is important to return (no necessary)
    # return None   # equivalent with no return statement


greeting = greet()
print(greeting)

print(len(greeting))
# TypeError: object of type 'NoneType' has no len()