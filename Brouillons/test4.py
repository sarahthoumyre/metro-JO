ligne_correspondantes = [['6', '9'], ['12', '8', '13'], ['12']]
numero_recherche = input("Entrez le numéro à chercher : ")  # Numéro que vous recherchez

numero_trouve = False

for sous_liste in ligne_correspondantes:
    if numero_recherche in sous_liste:
        numero_trouve = True
        break  # Arrête la boucle une fois que le numéro est trouvé

if numero_trouve:
    print(f"Le numéro {numero_recherche} est présent dans ligne_correspondantes.")
else:
    print(f"Le numéro {numero_recherche} n'est pas présent dans ligne_correspondantes.")