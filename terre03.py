lettre = input("Veuillez entrer une lettre : ")
resultat = ""

if len(lettre) != 1:
    print("Veuillez entrer une unique lettre de l'alphabet !")

elif ord(lettre) not in range(97, 123):
    print("Veuillez entrer une lettre de l'alphabet minuscule")
    
else:
    for i in range(ord(lettre), 123):
        resultat+=chr(i)
    print(resultat)
