# 143
# Add a Date Feature

# so when we run the program,
# we first will show the user the current date and time.
# It is Oct 07, 2024 00:16:20

# search for python date format codes
# from console:
# >>> time.strftime("%b %d, %Y %H:%M:%S")
# 'Oct 07, 2024 00:13:18'

# Python Module Index
# https://docs.python.org/3/py-modindex.html


import functions
# dir(functions)

import time

# dir(time)

now = time.strftime("%b %d, %Y %H:%M:%S")
# https://docs.python.org/3/library/time.html#time.strftime

print("It is", now)

while True:
    user_action = input('Type add, show, edit, complete or exit: ')    # Ajouter, Afficher or Quitter
    user_action = user_action.strip()


    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        # todos = get_todos()
        todos = functions.get_todos()   # import as module

        todos.append(todo)

        # write_todos(todos)
        # write_todos(filepath="todos.txt", todos_arg=todos)    # optional
        functions.write_todos(todos)   # import as module


    elif user_action.startswith('show'):
        # todos = get_todos()
        todos = functions.get_todos()   # import as module

        for index, item in enumerate(todos):
        # for index, item in enumerate(new_todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1     # list indexing starts from 0

            # todos = get_todos(filepath="todos.txt")   # optional
            # todos = get_todos()
            todos = functions.get_todos()   # import as module

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            # write_todos(todos)
            functions.write_todos(todos)   # import as module

        except ValueError:
            print("Your command is not valid. Try again!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            # todos = get_todos()
            todos = functions.get_todos()   # import as module
            # print(todos)
            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            # write_todos(todos)
            functions.write_todos(todos)       # import as module

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("The command is not valid.")

print("Bye!")