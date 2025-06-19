nombre = input("Veuillez entrer un nombre :")

if nombre.isdigit() == False:
    print("Tu ne me la mettras pas à l'envers")
elif int(nombre) % 2 == 0:
    print("pair")
else:
    print("impair")