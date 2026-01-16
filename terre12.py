import sys

#On gère les problèmes d'arguments
if len(sys.argv)!=2:
    sys.exit("Veuillez entrer un unique argument.")

elif len(sys.argv[1])!=7 or not (sys.argv[1][0]+sys.argv[1][1]+sys.argv[1][3]+sys.argv[1][4]).isdigit():
    sys.exit("Veuillez entrer un horaire au format HH:MMPM ou HH:MMAM")

elif  (sys.argv[1][5]!="P" or sys.argv[1][6]!="M") and (sys.argv[1][5]!="A" or sys.argv[1][6]!="M"):
    sys.exit("Veillez à préciser AM ou PM.")

elif int(sys.argv[1][0]+sys.argv[1][1])>12 or int(sys.argv[1][3]+sys.argv[1][4])>59:
        sys.exit("Veuillez respecter le format 12H et 60 minutes.")


#On transforme l'heure du format 24 au format 12 en distinguant 3 cas
#l'après-midi, le midi et le matin
moment=sys.argv[1][5]+sys.argv[1][6]
hour=int(sys.argv[1][0]+sys.argv[1][1])
minutes=int(sys.argv[1][3]+sys.argv[1][4])

if moment=="AM":
    print(f"{str(hour).zfill(2)}:{str(minutes).zfill(2)}")

elif hour==12 and moment=="PM":
    print(f"{str(hour-12).zfill(2)}:{str(minutes).zfill(2)}")

elif hour==0 and moment=="PM":
     print(f"{str(hour).zfill(2)}:{str(minutes).zfill(2)}")

else:
    print(f"{hour+12}:{str(minutes).zfill(2)}")