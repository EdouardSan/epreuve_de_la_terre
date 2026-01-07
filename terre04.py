import sys

#on teste qu'on ait bien un unique nombre entier en argument
if len(sys.argv)!=2 or sys.argv[1].isdigit()==False:
    sys.exit("Veuillez entrer en argument un unique nombre entier !")


else:
    number=int(sys.argv[1])
    if number%2 != 0:
        print(f"Le nombre {number} est impair.")
    else:
        print(f"Le nombre {number} est pair.")

    