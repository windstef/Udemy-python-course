# Nous allons commencer avec cette liste,
# et ensuite nous allons créer un programme qui sortira ces trois lignes ici.

# Donc le programme va trier les éléments par ordre alphabétique, comme vous le voyez

# Et nous allons également placer un numéro devant chacun des éléments ici dans la sortie.

waiting_list = ["sen", "ben", "john"]
waiting_list.sort()

# Et vous variez à la liste parce que comme je vous l('ai expliqué dans la vidéo précédente'
# 'les listes sont mutables.)
# Cela signifie que les méthodes vont modifier la liste.
# Donc la méthode elle-même ne renvoie pas ce que vous voyez ici.
# Retourner aucun.

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)


# autre moyen
# waiting_list = ["sen", "ben", "john"]
# for index, item in enumerate(sorted(waiting_list)):
#     row = f"{index + 1}.{item.capitalize()}"
#     print(row)


kg = float(input("Combien kg?"))
lbs = kg * 2.2
print(lbs)