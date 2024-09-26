# Nous voulons afficher des chiffres en face de chaque tâche
# à accomplir afin que l'utilisateur puisse simplement regarder le
# chiffre et l'écrire à cet endroit sans avoir à compter.


todos = []

while True:
    user_action = input('Type add, show, edit or exit: ')    # Ajouter, Afficher or Quitter
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo:')
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                # print(index, '-', item)
                row = f"{index}-{item}"
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
        case _: # Il est donc bon d'utiliser ce trait de soulignement, même si ce n'est pas nécessaire.
            print("He, vous entrez ne commande inconnue!")

print("Bye!")
