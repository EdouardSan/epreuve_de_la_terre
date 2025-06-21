# L'idée va être de manipuler une liste.
# On crée un nombre appelé "taille" qui va compter grâce à une boucle la taille de la liste
# La taille de cette liste sera égale à la taille de la chaîne.

chaine = input("Veuillez rentrer une chaîne de caractère : ")
taille = 0
liste_chaine = list(chaine)

# On gère les erreurs de l'utilisateur
if chaine.isspace():
    print("Erreur, entrez une chaîne de caractère et non des espaces !")

elif chaine.isdigit():
    print("Erreur, entrez une chaîne de caractère et non des chiffres !")

elif not chaine:
    print("Veuillez entrer une chaîne de caractère qui n'est pas vide !")

# Ici on compte le nombre d'élément de la liste
else:
    while liste_chaine:
            liste_chaine.pop(-1)
            taille+=1
    print(f"La taille de la chaîne de caractère est de {taille}.")



# Question pour Romain :
# Dans la boucle avec la condition 
# while liste_chaine == True      ca ne fonctionnait pas 
# mais avec while liste_chaine    ca marche : pourquoi ?
