# On prend chaque caractère et on les mets dans une liste
# A partir de cette liste facilement manipulable on remplit une chaine de caractère en inversant l'ordre

chaine = input("Entrez une chaîne de caractère : ")
liste_chaine = list(chaine)
chaine_inversee = ""

if len(chaine)<= 1:
    print("Veuillez entrer une chaîne de caractère viable")

elif chaine.isspace():
    print("Veuillez entrer une chaîne de caractère !")

else:
    for i in range(len(liste_chaine)):
        chaine_inversee += liste_chaine[-i-1]
    print(chaine_inversee)


# Question pour Romain :
# J'ai trouvé isspace() sur le manuel python, est-ce que cette méthode est de la triche ?