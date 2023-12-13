import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Liste des lieux
lieux = [
'stade-tour-eiffel',
'arena-champ-de-mars',
'grand-palais',
'invalides',
'hotel-de-ville',
'pont-alexandre-iii',
'trocadero', 
'la-concorde',
'stade-roland-garros',
'arena-paris-sud', 
'arena-bercy', 
'arena-la-chapelle', 
'paris-la-defense-arena', 
'centre-aquatique', 
'stade-de-france',
'site-escalade-bourget',
'arena-paris-nord'
]



# URLs correspondant à chaque lieu
urls = [
    f"https://www.paris2024.org/fr/site/{lieu.replace(' ', '-').lower()}/" for lieu in lieux
]
    
def get_specific_lines(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Recherche des lignes contenant les informations spécifiques
        specific_lines = []
        for paragraph in soup.find_all('p'):
            if 'Capacité' in paragraph.text or 'Capacité court Philippe-Chatrier' in paragraph.text or 'Volleyball' in paragraph.text or 'Pour la gymnastique rythmique' in paragraph.text:
                specific_lines.append(paragraph.text.strip())
        return specific_lines
    return None

# Création d'un dictionnaire pour stocker les résultats
results = {lieu: get_specific_lines(url) for lieu, url in zip(lieux, urls)}

# Création d'un DataFrame à partir du dictionnaire
df = pd.DataFrame(results.items(), columns=['Lieu', 'Informations'])

# Affichage du DataFrame
print(df)

#Compléter pour les valeurs manquantes : hôtel de ville
df.iloc[4, 1] = 45000

#Compléter pour les valeurs manquantes : arena-paris-sud
url = "https://fr.wikipedia.org/wiki/Arena_Porte_de_la_Chapelle"

# Obtenir le contenu de la page
response = requests.get(url)

if response.status_code == 200:
    # Analyser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Trouver le texte de la ligne commençant par "Capacité"
    capacity_text = soup.find("th", text="Capacité").find_next("td").get_text(strip=True)

    # Mettre à jour la case correspondante dans le DataFrame df
    df.iloc[7, 1] = capacity_text  # Ligne 8, colonne 2, indexées à partir de 0

    # Afficher le DataFrame mis à jour
    print(df)
else:
    print("La requête a échoué")


# Fonction pour extraire les nombres des listes de chaînes de caractères
def extract_numbers(text_list):
    if isinstance(text_list, list):
        numbers = []
        for text in text_list:
            num = re.findall(r'\d+', text)  # Trouve tous les groupes de chiffres
            if num:
                numbers.append(int(''.join(num)))  # Convertit la liste de chiffres en un nombre entier
        return numbers if numbers else None
    return None

# Appliquer la fonction à la colonne 'Informations' pour extraire les nombres
df['Informations'] = df['Informations'].apply(extract_numbers)

# Fonction pour extraire les quatre premiers chiffres d'une chaîne
def extract_first_four_digits(value):
    numbers = re.findall(r'\d{4}', str(value))  # Trouve les quatre premiers chiffres
    return int(numbers[0]) if numbers else None

# Appliquer la fonction à la colonne spécifique du DataFrame
df.iloc[:, 1] = df.iloc[:, 1].apply(extract_first_four_digits)  # Colonne 2, indexée à partir de 0

# Afficher le DataFrame mis à jour
display(df)