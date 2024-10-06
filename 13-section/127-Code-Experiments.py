# This experiment is about docstrings, which is these strings.

# Today, you'll learn that you can use
# these strings as documentation strings,
# also called docstrings, for functions.
# But these kind of strings, with these triple quotes,
# can also be used for another purpose.
# They can be used outside of functions
# and you can store them as you do normally in a variable.

def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        # yellow underlined todos: Shadows name 'todos' from outer scope. And it's not a good idea to have this variable with the same name as in function.
        # todos = file.readlines()
        todos_local = file_local.readlines()
    return todos_local

# docstring
# print(help(get_todos))


# no return anything, except of None. Behaves as procedure.
# with default argument/parameter
# Hint: non-default parameter must not follows default parameters
def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# docstring
# print(help(write_todos))

# docstrings, multi-line strings with triple quotes. (without \n)
text = """
Principles of productivity:
Managing your inflow.
Systemizing everything that repeats.
"""


# with strings, then breaklines must be typed:
# text = "\
# Principles of productivity: \n\
# Managing your inflow.\n\
# Systemizing everything that repeats.\
# "

print(text)

while True:
    user_action = input('Type add, show, edit, complete or exit: ')    # Ajouter, Afficher or Quitter
    user_action = user_action.strip()


    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)
        # write_todos(filepath="todos.txt", todos_arg=todos)    # optional

    elif user_action.startswith('show'):
        todos = get_todos()

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
            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid. Try again!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            # print(todos)
            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            write_todos(todos)

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