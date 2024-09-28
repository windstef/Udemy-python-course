# Dans cette vidéo, nous allons examiner un autre exemple de boucle sauvage afin que vous compreniez la boucle
# sauvage sous un autre angle.

password = input("Entrez le mot de passe: ")

while password != "pass123":
    password = input("Entrez le mot de passe")

print("Le mot de passe etait correct!")