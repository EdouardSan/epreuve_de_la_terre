import sys

#On vérifie qu'il n'y a qu'un argument et qu'il s'agit d'une lettre de l'alphabet
if len(sys.argv)!=2:
    sys.exit("Veuillez entrer en argument une unique lettre de l'alphabet !")

elif ord(sys.argv[1])<97 or ord(sys.argv[1])>122:
    sys.exit("Veuillez entrer en argument une lettre de l'alphabet en minuscule !")

else:
    #La boucle pour créer l'alphabet partiel
    alphabet_size=range(ord(sys.argv[1]), ord("z")+1)
    alphabet=""

    for i in alphabet_size:
        alphabet+=f"{chr(i)}"
    
    print(alphabet)