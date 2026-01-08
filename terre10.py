import sys

#On gère les problèmes d'arguments et les cas particuliers 
if len(sys.argv)!=2:
    sys.exit("Veuillez entrer un unique nombre entier")

elif sys.argv[1]=="1" or sys.argv[1]=="0":
    sys.exit("Attention 1 et 0 ne sont pas des nombres premiers.")

elif not sys.argv[1].isdigit():
    sys.exit("Veuillez entrer un nombre entier positif")

#La boucle pour trouver si le nombre est premier
is_prime_number=int(sys.argv[1])
for number in range(2, is_prime_number):

    if is_prime_number%(number)==0:
        sys.exit(f"Non, {is_prime_number} n'est pas un nombre premier.")
    else:
        continue

print(f"Oui, {is_prime_number} est un nombre premier")