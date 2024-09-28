# Nous allons créer une application de journal quotidien qui se comporte comme ceci.
#
# Laissez-moi vous montrer le résultat du programme.
#
# Le programme demande d'abord à l'utilisateur de saisir la date du jour.
#
# Alors entrons en 2022 et 10, peut-être 20.
#
# Vous appuyez sur le bouton "Entrée" du programme, qui vous demande à nouveau d'évaluer vos humeurs - l'humeur que vous aviez aujourd'hui - de 1 à 10.
#
# Répondons à huit, par exemple, et ensuite vous écrivez les pensées du jour.
#
# Alors écrivons quelque chose comme "c'était une bonne journée en général".
#
# Aucun événement important n'a eu lieu.
#
# Appuyez sur la touche Entrée.
#
# C'est tout.
#
# Maintenant, si vous allez dans le répertoire du journal, que j'avais créé plus tôt,
# donc vous devez créer ce répertoire manuellement.
#
# Et puis à l'intérieur de ça, un fichier a été généré par Python.

# Ainsi, chaque nouveau jour où vous exécutez le programme, il créera un nouveau fichier.
# Donc dix jours, dix fichiers, et chaque fichier contiendra la date du jour comme nom de fichier.

#### Sortie ####
# Enter today's date: 2022-10-20
#
# How do you rate your mood from 1 to 10? 8
#
# Let your thoughts flow:
# It was a good day in general. No big events happened.

# fichier: ../journal/2022-10-20.txt
# exemple du contenu:
# 7
#
# Tout est bien!


date = input("Enter today's date: ")

mood = input("How do you rate your mood from 1 to 10? ")

thoughts = input("Let your thoughts flow:\n")

with open(f"journal/{date}.txt", "w") as file:
    # file.write(mood + "\n" + "\n")
    file.write(mood + 2 * "\n")
    file.write(thoughts)

