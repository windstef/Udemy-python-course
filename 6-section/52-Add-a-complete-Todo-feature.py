# Dans cette vidéo, nous allons ajouter une fonctionnalité complète à notre programme,
# complète signifiant permettre à l'utilisateur
# de marquer un élément à faire comme complet ou fait.
# Ainsi, cet élément sera supprimé de la liste des choses à faire.


todos = []

while True:
    user_action = input('Type add, show, edit, complete or exit: ')    # Ajouter, Afficher or Quitter
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo:')
            todos.append(todo)
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
