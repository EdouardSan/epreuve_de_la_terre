import sys

#On gère les problèmes d'arguments
if len(sys.argv)!=2:
    sys.exit("Veuillez entrer un unique argument.")

elif len(sys.argv[1])!=5 or not (sys.argv[1][0]+sys.argv[1][1]+sys.argv[1][3]+sys.argv[1][4]).isdigit():
    sys.exit("Veuillez entrer un horaire au format HH:MM")

else:
    hour=int(sys.argv[1][0]+sys.argv[1][1])
    minutes=int(sys.argv[1][3]+sys.argv[1][4])
    if hour>23 or minutes>59:
        sys.exit("Veuillez respecter le format 24H et 60 minutes.")

#On transforme l'heure du format 24 au format 12 en distinguant 3 cas
#l'après-midi, le midi et le matin
if hour>=13:
    hour-=12
    print(f"{str(hour).zfill(2)}:{str(minutes).zfill(2)}PM")
elif hour==12:
    print(f"{str(hour).zfill(2)}:{str(minutes).zfill(2)}PM")
else:
    print(f"{str(hour).zfill(2)}:{str(minutes).zfill(2)}AM")