lettre = input("Veuillez entrer une lettre : ")
resultat = ""

# On s'assure que l'utilisateur rentre une seule lettre minuscule
if len(lettre) != 1:
    print("Veuillez entrer une unique lettre de l'alphabet !")

elif ord(lettre) not in range(97, 123):
    print("Veuillez entrer une lettre de l'alphabet minuscule")

# Une fois bon on affiche la fraction de l'alphabet en question
else:
    for i in range(ord(lettre), 123):
        resultat+=chr(i)
    print(resultat)
