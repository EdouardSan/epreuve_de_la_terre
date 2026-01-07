import sys

#on nomme les choses et on utilisera une liste pour les manipulations
chain=sys.argv[1]
chain_list = list(chain)
inverted_chain = ""

#On gère les erreurs d'arguments
if len(sys.argv)>2:
    sys.exit("Veuillez n'entrer qu'une seule chaine de caractère !")

elif len(chain)<= 1:
    sys.exit("Veuillez entrer une chaîne de caractère viable")

elif chain.isspace():
    sys.exit("Veuillez entrer une chaîne de caractère !")

#La boucle qui inverse la chaîne de caractère 
else:
    for i in range(len(chain_list)):
        inverted_chain+=chain_list[-i-1]
    print(inverted_chain)



