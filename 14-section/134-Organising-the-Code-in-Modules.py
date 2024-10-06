# 134
# Organising the Code in Modules

# following:

# 126
# Documenting the Code

# 125
# Optimising the code
# section: App 1 - Build a Todo List App | #default-arguments

# 116: Avoiding Repetitive Code #custom-functions

# Objective:
# docstrings

# example:
# python console
# >>> help(len)
# Help on built-in function len in module builtins:
# len(obj, /)
#     Return the number of items in a container.

# the last is the docstring


#############
# import the interesting functions from the file 'functions.py'
# from functions import get_todos, write_todos

# other way to import functions, as module
# from modules import functions     # if located under dir modules/
import functions

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