# Ce que l'utilisateur entre
nombre = input("Entrez un nombre : ")
puissance = input("Entrez une puissance : ")

# Les cas de défaut utilisateur
if (not nombre or not puissance) or (not nombre and not puissance):
    print("Veuillez entrer un nombre et une puissance.")

elif nombre.isspace() or puissance.isspace():
    print("Veuillez n'entrer qu'un seul nombre à la fois ou evitez les espaces.")

elif not nombre.isdigit() or not puissance.isdigit():
    print("Veuillez n'entrer que des nombres !")

# Le résultat qui s'affiche en entier dans un f-string
else:
    print(f"Le résultat de {nombre} à la puissance {puissance} est : {int(nombre)**int(puissance)}")


