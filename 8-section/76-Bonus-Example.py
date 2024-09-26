# Dans l'exemple d'aujourd'hui, nous allons transformer cette liste de noms de fichiers en ceci.
# ["1.doc", "1-report", "1.presentation"]

# C'est donc la sortie du programme.
# ['1-doc.txt', '1-report.txt', '1-presentation.txt']

# Donc aujourd'hui, nous allons simplement travailler sur la transformation des cordes.

filenames = ["1.doc", "1-report", "1.presentation"]
print(filenames)


# Ainsi, lorsque vous voulez transformer une liste, ce que vous pensez est une compréhension de la liste.

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)
