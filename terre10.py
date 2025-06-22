# Ici on a le nombre dont on cherche la racine carrée 
# et un compteur qui s'activera quand un diviseur du nombre sera trouvée
# Donc si le compteur est activée alors le nombre n'est pas premier

nombre = input("Entrez un nombre : ")
compteur=0

# On gère ici les cas particuliers et les cas de défaut utilisateur
if not nombre:
    print("Veuillez entrer un nombre.")

elif nombre.isspace():
    print("Veuillez eviter les espaces.")

elif not nombre.isdigit():
    print("Veuillez n'entrer que des nombres !")

elif nombre == "1" or nombre == "0":
    print(f"{nombre} n'est pas un nombre premier !")

else:
    # On part de 2 car on ne divise pas par 0 et tous sont déjà divisible par 1
    for i in range(2, int(nombre)):
        if int(nombre)%i == 0:
            compteur+=1
        elif i == int(nombre)-1 and compteur != 0:
            print(f"{nombre} n'est pas un nombre premier")
        elif i == int(nombre)-1 and compteur == 0:
            print(f"{nombre} est un nombre premier")