
# 1
# C'était donc la première chose que je voulais vous montrer : les chemins d'accès aux fichiers doivent exister
# lorsque vous ouvrez un fichier en mode lecture.

# with open("files/docs.txt", "r") as file:
#     file.read()


# 2
# Eh bien, c'est parce que par défaut, la fonction d'ouverture.
# Attribue une valeur r à l'argument modes afin que vous puissiez ouvrir une console python.
# Et vérifiez l'aide pour l'ouverture.
# >>> help(open)

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#     Open file and return a stream.  Raise OSError upon failure.
# 'r'       open for reading (default)

# with open("files/docs.txt") as file:
#     print(file.read())



# 3

# Ainsi, le gestionnaire de contexte avec
# ne vous oblige pas à avoir des méthodes de libération de fichiers ici.

# with open("files/docs.txt") as file:
#     print("Bonsoir")
# file.read()

#   File "/home/stefkour/PycharmProjects/app1/pythonProject/9-section/84-Code-Experiments.py", line 32, in <module>
#     file.read()
# ValueError: I/O operation on closed file.



# 4

# Et enfin, la dernière chose que je veux détruire est que vous le savez déjà, mais je voulais le souligner,
# qu'une fois que vous avez assigné la variable au fichier, lisez.
# Méthodes, vous pouvez alors utiliser la variable autant de fois que vous le souhaitez.
# Vous exécutez donc les scripts et la variable sera imprimée autant de fois
# qu'il y a de fonctions d'impression ici.

with open("files/docs.txt") as file:
    file.read()
    content = file.read()

print(content)
print(content)



# Donc, dans ce cas, nous n'obtenons aucune sortie.
# C'est parce que la chaîne est d'abord créée ici par la méthode de lecture, puis la méthode de lecture est épuisée.
# Donc la deuxième fois, elle renvoie un écran vide, parce que comme je l'ai expliqué la première fois, la bonne
# méthode lit la chaîne jusqu'ici, le contenu du fichier texte, elle le lit jusqu'ici.
# Et ensuite, si vous exécutez à nouveau la méthode de lecture, elle essaie de lire ce qui se trouve à la fin ici.
# Il n'y a donc rien de permanent.
#
# C'est pourquoi vous obtenez une chaîne vide.