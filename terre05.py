import sys

#on vérifie que deux nombres entiers ont été entrés en argument
if len(sys.argv)!=3 or sys.argv[1].isdigit()==False or sys.argv[2].isdigit()==False:
    sys.exit("Veuillez entrer en argument deux nombres entiers !")

else:
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    if b==0 or a<b:
        sys.exit("erreur.")
    else:
        print(f"""resultat : {a//b}\nreste : {a%b}""")
        

    
