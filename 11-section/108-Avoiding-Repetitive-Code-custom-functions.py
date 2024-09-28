# 108
# Avoiding Repetitive Code #custom-functions

# Objective:
# You will learn one of the most important elements of Python
# and that is custom functions.
# So let's look at our code and see how custom functions will improve our program.
# Because currently, we have a problem with the program,
# and the problem is redundancy.

##############
# Built-in functions
#ex. input(), open()
# Go to Implementation


# And then down here, you have pass.
# So you don't actually see the code here,

# And that is because all these functions, so open and input, these were written in C language.

# So C is the language used to write the interpreter of Python.

# Remember, when we installed the interpreter from python.org,
# that is a program which interprets Python language and that program is written in C language.

# So all these functions are actually written in C language and we cannot see the code.

#############

def get_todos():
    # context manager
    with open('todos.txt', 'r') as file_local:
        # yellow underlined todos: Shadows name 'todos' from outer scope. And it's not a good idea to have this variable with the same name as in function.
        # todos = file.readlines()
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input('Type add, show, edit, complete or exit: ')    # Ajouter, Afficher or Quitter
    user_action = user_action.strip()


    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

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

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
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

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

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