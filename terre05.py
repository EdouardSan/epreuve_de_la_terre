nombre_a = input("Veuillez entrer un premier nombre : ")
nombre_b = input("Veuillez entrer un deuxième nombre : ")

if nombre_a.isdigit() == False or nombre_b.isdigit() == False:
    print("Veuillez rentrer des nombres valides")
else:
    resultat = int(nombre_a)//int(nombre_b)
    reste = int(nombre_a)%int(nombre_b)
    print(f"""Le résultat est : {resultat}.
Le reste est : {reste}.""")