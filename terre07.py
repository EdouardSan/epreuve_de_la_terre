import sys

#On gère les erreurs d'arguments
if len(sys.argv)!=2:
    sys.exit("erreur.")

elif sys.argv[1].isdigit():
    sys.exit("erreur.")

#On parcourt la chaîne de caractère et on incrémente la taille de cette dernière au 
#fur et à mesure de son parcours
else:
    chain_size=0
    chain=sys.argv[1]

    for caracter in chain:
        chain_size+=1
    print(chain_size)