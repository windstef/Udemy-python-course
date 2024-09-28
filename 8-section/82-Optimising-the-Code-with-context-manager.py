# Cette vidéo est l'une de ces vidéos où nous n'améliorons pas le résultat du programme,
# mais nous améliorons le code.

#Nous allons rendre le code plus lisible, plus efficace.
# Donc rien sur la sortie ne changera.

# Ce que nous allons faire exactement est
# d'utiliser une meilleure façon de gérer les fichiers.

# Ainsi, par exemple, ici nous ouvrons un fichier en mode lecture puis nous lisons les lignes de ce fichier texte.
# Nous stockons les lignes dans les listes et ensuite nous fermons le fichier.
# Mais cela peut être fait d'une meilleure manière en utilisant le gestionnaire de contexte with.



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
            # print("Je l'ai")
            number = int(input("Number of the todo to edit: "))
            # existing_todo = todos[number]
            number = number - 1     # list indexing starts from 0
            print(todos[number])
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
            print(todos[number])
        case 'exit':
            break
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number-1)
        case _: # Il est donc bon d'utiliser ce trait de soulignement, même si ce n'est pas nécessaire.
            print("He, vous entrez ne commande inconnue!")

print("Bye!")
