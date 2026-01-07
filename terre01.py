import sys

file_name=""
file_path=sys.argv[0]

#character parcours le chemin d'accès. A chaque fois qu'on tombe sur un "/" on efface le nom du fichier.
#Les derniers caractères rentrés dans file_name sont le nom du fichier
for character in file_path:
    if character == "/":
        file_name=""
    else:
        file_name+=character

print(file_name)