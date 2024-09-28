# 117
# Optimising the code Further
# follow the:
# 116: Avoiding Repetitive Code #custom-functions - Optimising the code

# Objective:
# Functions with multiple arguments.

#############

# input: filepath (parameter)
def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        # yellow underlined todos: Shadows name 'todos' from outer scope. And it's not a good idea to have this variable with the same name as in function.
        # todos = file.readlines()
        todos_local = file_local.readlines()
    return todos_local

# no return anything, except of None. Behaves as procedure.
def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)



while True:
    user_action = input('Type add, show, edit, complete or exit: ')    # Ajouter, Afficher or Quitter
    user_action = user_action.strip()


    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        todos = get_todos("todos.txt")

        todos.append(todo)

        write_todos("todos.txt", todos)
        # write_todos(filepath="todos.txt", todos_arg=todos)    # optional

    elif user_action.startswith('show'):
        todos = get_todos("todos.txt")

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
            todos = get_todos("todos.txt")

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos("todos.txt", todos)

        except ValueError:
            print("Your command is not valid. Try again!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos("todos.txt")
            # print(todos)
            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            write_todos("todos.txt", todos)

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