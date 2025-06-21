# On passe ici d'un string à une liste qui est plus facilement manipulable
arguments = input("Entrez ce que vous voulez : ")

liste_arguments = arguments.split(" ")

for i in range(len(liste_arguments)):
    print(liste_arguments[i])
    