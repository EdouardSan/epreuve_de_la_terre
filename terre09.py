# Ici on a le nombre dont on cherche la racine carrée 
# et un compteur qui s'activera quand une racine carrée sera trouvée
nombre = input("Entrez un nombre : ")
compteur=0

# On gère ici les cas particuliers et les cas de défaut utilisateur
if not nombre:
    print("Veuillez entrer un nombre.")

elif nombre.isspace():
    print("Veuillez éviter les espaces.")

elif not nombre.isdigit():
    print("Veuillez n'entrer que des nombres !")

elif int(nombre) == 0:
    print("La racine carré de 0 est égale à 0.")

elif int(nombre) == 1:
    print("La racine carrée de 1 est égale à 1.")


# Ici on a un compteur qui s'active quand une racine carré a été trouvée.
# Arrivé au bout de la boucle si le compteur à racine carré ne s'est pas activé...
# -->pas de racine entière existante!
elif int(nombre) > 1:
    for i in range(int(nombre)):
        if i**2 == int(nombre):
            print(f"La racine carré de {nombre} est {i}.")
            compteur+=1

        elif (i == int(nombre)-1) and (compteur == 0):
            print(f"{nombre} n'a pas de racine carrée entière !")
            


