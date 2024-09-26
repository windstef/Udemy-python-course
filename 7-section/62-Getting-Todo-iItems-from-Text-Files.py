# Maintenant, si vous avez des données plus complexes, vous pouvez utiliser le format CSV,
# donc des fichiers CSV ou JSON, et si vous
# avez des données encore plus complexes où il y a plus d'interaction de l'utilisateur avec les données,
# alors vous pouvez opter
# pour la solution ultime, à savoir les bases de données SQL.
# Nous allons donc couvrir toutes ces technologies dans le cours.
# Concentrons-nous maintenant sur les fichiers texte.


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
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
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


#####################

# Voilà donc comment lire un fichier absolu sous Linux.

# Ainsi, Mac et Linux utilisent quatre barres obliques.

# Windows: Vous devez utiliser les barres obliques inverses

# par exemple chemin du fichier:
# /home/stefkour/Documents/neo4j-db-stufftxt.txt


# file = open("/home/stefkour/Documents/neo4j-db-stufftxt.txt", "r")
# file.readlines()
# ['neo4j\n', '\n', 'http://localhost:7474/browser/\n', '\n', 'db: neo4j (neo4j_1)\n', '\n', 'username: neo4j\n', '\n', 'pwd: neo4j0824\n', '\n', '\n', '\n', '- useful\n', '\n', 'https://www.geeksforgeeks.org/neo4j-introduction/#what-is-neo4j\n', '\n', 'https://neo4j.com/docs/operations-manual/current/docker/introduction/\n', '\n', 'https://hub.docker.com/_/neo4j\n', '\n', '\n', '> docker container\n', '\n', 'stefkour@stefkour:~$ sudo docker start suspicious_sutherland\n', '\n']
