# Expérimentons maintenant un peu avec le code afin de mieux comprendre certains aspects de Python.


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
                row = f"{index + 1}-{item}"     # commencer la liste à partir de un et non de zéro.
                print(row)
            print(f"Longeur de la liste est {index + 1}")
            print(len(todos))       ## Experiment 2: len()
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1     # list indexing starts from 0
            print(todos[number])
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
            print(todos[number])
        case 'exit':
            # print("Exit: Longeur de la liste: ", index + 1)
            break
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number-1)
        case _: # Il est donc bon d'utiliser ce trait de soulignement, même si ce n'est pas nécessaire.
            print("He, vous entrez ne commande inconnue!")

print("Bye!")


## Experiment 3: enumerate()

# Les chaînes peuvent donc également être utilisées avec la fonction énumérer,
# car les chaînes sont également des séquences d'éléments et chaque
# élément est lui-même une chaîne.

# >> python console
#
# for i, j in enumerate("Bonjour"):
#     print(i, j)

# 0 B
# 1 o
# 2 n
# 3 j
# 4 o
# 5 u
# 6 r


# >>> a = enumerate(["a", "b", "c"])
# >>>  a
# <enumerate object at 0x73272f9ebce0>

# >>>  list(a)
# [(0, 'a'), (1, 'b'), (2, 'c')]


# Donc enumerate est une liste de tuples et vous dites
# print I item press enter, enter et on obtient ceci.

# >>> for i, item in [(0, 'a'), (1, 'b'), (2, 'c')]:
#     print(i, item)

# 0 a
# 1 b
# 2 c


# Bien sûr, vous pouvez faire la même chose avec une chaîne de caractères.

# >>> b = enumerate("Hello")
# >>> list(b)
# [(0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

# >>> str(b)
# '<enumerate object at 0x73272f611120>'
