# 99
# Fixing Two Bugs in the Program #bugs


# first bug: add command. Fix by insert a breakline

# secong bug: add command.
# scenario: 'edit add a new member' :: add treated as command not as todo item (expected)
# solution: not check for an add command anywhere in the string.
# Replace if 'add' in user_action: with if user_action.startswith('add'):
# similar for the other elif conditions

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
        # number = int(input("Number of the todo to edit: "))
        number = int(user_action[5:])
        number = number - 1     # list indexing starts from 0

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        # print('Les choses à faire existants dans la liste: ', todos)

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        # print('Voici comment cela va se passer: ', todos)
        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)

    elif user_action.startswith('complete'):
        # number = int(input("Number of the todo to complete: "))
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

    elif user_action.startswith('exit'):
        break

    else: # Il est donc bon d'utiliser ce trait de soulignement, même si ce n'est pas nécessaire.
        print("The command is not valid.")

print("Bye!")