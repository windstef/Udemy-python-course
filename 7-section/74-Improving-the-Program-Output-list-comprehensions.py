# Dans cette vidéo, nous allons rendre notre programme un peu plus convivial parce qu'actuellement
# nous avons ces lignes de rupture ici, ce qui n'est pas très agréable du point de vue de l'utilisateur.
# Supprimons donc ces lignes de rupture.

# La ligne de rupture supplémentaire est donc produite par la fonction d'impression ici.

while True:
    # Obtenir l'entrée de l'utilisateur et supprimer ou et strip caractères de l'espace.
    user_action = input('Type add, show, edit, complete or exit: ')    # Ajouter, Afficher or Quitter
    user_action = user_action.strip()

    match user_action:
        # Verifier si l'action de l'utilisateur est 'Ajouter' (Add)
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
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # new_todos = []
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            # print(todos)
            # ['montrer\n', 'ajouter\n', 'lire\n', 'ecrire\n', 'nettoyer\n', 'marcher\n']

            # print(new_todos)

            # Une autre façon de nettoyer la liste est d'utiliser une compréhension de liste
            # new_todos = [item.strip('\n') for item in todos]


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
