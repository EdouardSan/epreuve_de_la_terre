#!/usr/bin/env python3

# Sur conseil de Romain on utilise le code ASCII décimal gràce à la fonction chr
resultat = ""

for i in range(97, 123):
    resultat+=chr(i)
print(resultat)