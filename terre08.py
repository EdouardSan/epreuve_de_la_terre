import sys

#On gère les problèmes d'arguments et les cas particuliers
if len(sys.argv)!=3:
    sys.exit("Veuillez entrer 2 nombres en argument.")

elif sys.argv[1].isdigit()==False or sys.argv[2].isdigit()==False:
    sys.exit("Veuillez entrer des nombres entiers positifs")

elif sys.argv[2]=="1":
    sys.exit(sys.argv[1])

elif sys.argv[2]=="0":
    print(1)

#On réalise l'opération
else:
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    result=1
    for power in range(b):
        result*=a
    print(result)

