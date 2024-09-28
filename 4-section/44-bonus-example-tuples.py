filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

# list (mutable)

# string (immutable)

# Supposons donc que nous ayons un dossier ici, et que ce dossier contienne trois fichiers texte avec ces
# noms, et que nous voulions changer le point de chaque nom de fichier en tiret.


# Est-ce vraiment impossible parce que les chaînes de caractères sont immuables ?

# for filename in filenames:
#     filename = filename.replace('.', '-', 1)
#     print(filename)


# tuples (immutables)

# filenames_t = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt")

# type(filenames_t)
# <class 'tuple'>



###############################

# Coding Exercise 1
# Create a program that:
#
# 1. Prompts the user to input a (dollar) amount.
#
# 2. Calculates the corresponding amount in euros, given an exchange rate of 2.
#
# 3. Prints out the amount in euros.

rate = 2

dollar = input("Enter an amount in dollar: ")

euro = int(dollar) * rate

print(euro)