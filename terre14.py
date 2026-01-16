import sys

#On crée la liste composé des chaînes de caractère avec les nombres
#On initialise la liste composé des nombre de type <int>
list_string=sys.argv
list_string.pop(0)
list_number=[]

# On gère les problèmes d'arguments
for string in list_string:
    if not string.isdigit():
        sys.exit("Erreur !")
    else:
        continue

#On crée une liste d'entier à partir de la liste des arguments en string
for number in list_string:
    list_number+=[int(number)]


#On parcourt la liste pour savoir si les nombres sont classés
for i in range(len(list_number)):
    if i==len(list_number)-1:
        sys.exit("Triée !")
    elif list_number[i]>list_number[i+1]:
        sys.exit("Pas triée !")
        continue

