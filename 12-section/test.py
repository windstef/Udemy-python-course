def greet():
    message = "hello"
    new_message = message.capitalize()
    return new_message

greeting = greet()
print(greeting)

new_message = greet()
print(new_message)

# variable scope
# print(new_message)
# NameError: name 'new_message' is not defined
