
todos = []

# while True:
#     user_action = input('Type add, show, or exit: ')    # Ajouter, Afficher or Quitter
#     user_action = user_action.strip()
#
#     match user_action:
#         case 'add':
#             todo = input('Enter a todo:')
#             todos.append(todo)
#         case 'show':
#             for item in todos:
#                 print(item)
#         case 'exit':
#             break
#         case _: # Il est donc bon d'utiliser ce trait de soulignement, même si ce n'est pas nécessaire.
#             print("He, vous entrez une commande inconnue!")
#
# print("Bye!")


while True:
    user_action = input('Type add, show, or exit: ')    # Ajouter, Afficher or Quitter
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo:')
            todos.append(todo)
        # case 'show' | 'display':
        case 'show':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break

print("Bye!")