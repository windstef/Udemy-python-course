
todos = []

while True:
    user_action = input('Type add, show, edit or exit: ')    # Ajouter, Afficher or Quitter
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo:')
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
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
        case _: # Il est donc bon d'utiliser ce trait de soulignement, même si ce n'est pas nécessaire.
            print("He, vous entrez ne commande inconnue!")

print("Bye!")

print("Au revoir!")


# Vous avez donc appris dans cette vidéo comment convertir une chaîne de caractères en un nombre.
# En utilisant cette fonction, vous apprenez également comment accéder aux éléments d'une liste à l'aide de cette syntaxe, et vous apprenez également
#
# comment remplacer un élément à l'aide de cette syntaxe.
