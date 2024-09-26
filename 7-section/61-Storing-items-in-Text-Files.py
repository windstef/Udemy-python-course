# Maintenant, si vous avez des données plus complexes, vous pouvez utiliser le format CSV,
# donc des fichiers CSV ou JSON, et si vous
# avez des données encore plus complexes où il y a plus d'interaction de l'utilisateur avec les données,
# alors vous pouvez opter
# pour la solution ultime, à savoir les bases de données SQL.
# Nous allons donc couvrir toutes ces technologies dans le cours.
# Concentrons-nous maintenant sur les fichiers texte.


# todos = []

while True:
    user_action = input('Type add, show, edit, complete or exit: ')    # Ajouter, Afficher or Quitter
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo:') + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            for index, item in enumerate(todos):
                # print(index, '-', item)
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
