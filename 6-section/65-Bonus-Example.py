# Nous allons donc écrire un programme, et lorsque nous exécutons ce programme,
# celui-ci va générer cestrois fichiers dans le répertoire files.
# Et chacun de ces fichiers va contenir.
# Le contenu correspondant.
# Le premier fichier va donc contenir ce premier contenu.
# Le deuxième fichier va contenir ce deuxième contenu et
# le troisième fichier va contenir le troisième contenu.


contents = ["All carrots are to be slices "
            "longitudinally",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

# for boucle (loop)
# utiliser: zip function
# exemple:

# a = [1, 2, 3]
# b = [10, 20, 30]
# x = zip(a, b)
# x
# <zip object at 0x78c5b4d6bfc0>
# list(x)
# [(1, 10), (2, 20), (3, 30)]

# Mais si vous le convertissez en liste, comme nous l'avons fait avec l'objet enumerate, alors vous obtenez ceci.
# Représentation, qui est la même structure que celle de l'objet énuméré.
# La différence est que les premiers éléments sont les éléments réels de la première liste, et les seconds
# sont les éléments de la seconde liste.

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)


## ##

# C'est donc le cas lorsque vous avez des chaînes de caractères très longues
# qui dépassent l'espace horizontal de votre éditeur.

# Et il devient utile de les diviser comme ça.
# Le code reste donc plus facile à voir, à lire et à gérer.

a = "I am a string on my own"
print(a)

b = "I am a string " \
    "on my own. " \
    "(splitted in the programme)"

print(b)
