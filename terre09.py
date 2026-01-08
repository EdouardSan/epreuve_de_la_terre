import sys

#On gère les problèmes d'arguments
if len(sys.argv)!=2:
    sys.exit("Veuillez entrer un unique nombre entier en argument.")

elif not sys.argv[1].isdigit():
    sys.exit("erreur.")

#La boucle pour calculer la racine carrée
number=int(sys.argv[1])
root_number=0
while root_number<=number:
    if root_number**2==number:
        sys.exit(print(root_number))
    else:
        root_number+=1
        continue


