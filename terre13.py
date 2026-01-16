import sys

#On gère les problèmes d'arguments
if len(sys.argv)!=4:
    sys.exit("Veuillez entrer 3 nombres entiers")

elif not (sys.argv[1]+sys.argv[2]+sys.argv[3]).isdigit():
    sys.exit("Veuillez entrer des nombres entiers positifs.")
    
elif sys.argv[1]==sys.argv[2] or sys.argv[1]==sys.argv[3] or sys.argv[2]==sys.argv[3]:
    sys.exit("Veuillez entrer des nombres entiers positifs différents.")

#On tri par insertion
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])

if a<b<c:
    print(f"{b}")

elif c<b<a:
    print(f"{b}")

elif b<a<c:
    print(f"{a}")

elif c<a<b:
    print(f"{a}")

elif a<c<b:
    print(f"{c}")

else:
    print(f"{c}")




