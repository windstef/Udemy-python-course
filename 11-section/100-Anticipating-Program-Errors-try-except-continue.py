# 100
# Anticipating Program Errors
# try-except-continue

# case:
# if the user enters edit, and then instead of entering a number
# they enter a todo item, the program will end abruptly.
# And that is not a good user experience.

# Type add, show, edit, complete or exit: edit add a new
# Traceback (most recent call last):
#   File "/home/stefkour/PycharmProjects/app1/pythonProject/11-section/99-Fixing-Two-Bugs-in-the-Program-bugs.py", line 47, in <module>
#     number = int(user_action[5:])
#              ^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'add a new'

# case:
# the user tries to complete an item
# which is not in the list, for example, item 23,
# when all we have is a few items,
# and in that case we will get an index error.

# Type add, show, edit, complete or exit: complete 23
# Traceback (most recent call last):
#   File "/home/stefkour/PycharmProjects/app1/pythonProject/11-section/100-Anticipating-Program-Errors-try-except-continue.py", line 85, in <module>
#     todo_to_remove = todos[index].strip('\n')
#                      ~~~~~^^^^^^^
# IndexError: list index out of range


# Solution:
# So what we want instead is if the user enters this,
# we will tell the user that they entered the wrong command
# and then we will let the user enter the command again by showing them this prompt.
# Type add, show, edit, complete or exit!

# Use of error handling

while True:
    # Obtenir l'entrée de l'utilisateur et supprimer ou et strip caractères de l'espace.
    user_action = input('Type add, show, edit, complete or exit: ')    # Ajouter, Afficher or Quitter
    user_action = user_action.strip()


    # if 'add' in user_action:
    if user_action.startswith('add'):
        # todo = input('Enter a todo:') + "\n"
        todo = user_action[4:] + "\n"

        # context manager (recommandé)
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

# context manager: Vous n'avez pas besoin de fermer le fichier.'

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
        # for index, item in enumerate(new_todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"     # commencer la liste à partir de un et non de zéro.
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1     # list indexing starts from 0

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

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

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
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

    else: # Il est donc bon d'utiliser ce trait de soulignement, même si ce n'est pas nécessaire.
        print("The command is not valid.")

print("Bye!")