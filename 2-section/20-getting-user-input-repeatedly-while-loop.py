## Section 3: Day 2 - App 1: Build a To-do App with Python (Methods and While-Loop) ##


# 20. Geting User Input Repeatedly #while-loop #

# user_prompt = "Enter a todo:"
#
# while True:
#     todo = input(user_prompt)
#     print(todo)
#     print("Suivant ...")



# 22. Storing User Input Repeatedly #methods

user_prompt = "Enter a todo:"

todos = []

while True:
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)
    print(todos)
