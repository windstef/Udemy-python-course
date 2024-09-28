# Dans cette vidéo, nous allons travailler sur le montage et le cas complet.



while True:
    # Obtenir l'entrée de l'utilisateur et supprimer ou et strip caractères de l'espace.
    user_action = input('Type add, show, edit, complete or exit: ')    # Ajouter, Afficher or Quitter
    user_action = user_action.strip()

    match user_action:
        # Verifier si l'action de l'utilisateur est 'Ajouter' (Add)
        case 'add':
            todo = input('Enter a todo:') + "\n"

            # context manager (recommandé)
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

# Vous n'avez pas besoin de fermer le fichier.'

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
            # for index, item in enumerate(new_todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"     # commencer la liste à partir de un et non de zéro.
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1     # list indexing starts from 0

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            # print('Les choses à faire existants dans la liste: ', todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            # print('Voici comment cela va se passer: ', todos)
            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

        case 'exit':
            break

        case 'complete':
            number = int(input("Number of the todo to complete: "))
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            # print(todos)
            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)
            # print(todos)

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        case _: # Il est donc bon d'utiliser ce trait de soulignement, même si ce n'est pas nécessaire.
            print("He, vous entrez ne commande inconnue!")

print("Bye!")
