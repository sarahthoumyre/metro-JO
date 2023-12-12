import geopandas as gpd
import requests
import io
import matplotlib.pyplot as plt

# URL directe du fichier CSV sur GitHub
url = "https://data.iledefrance-mobilites.fr/api/explore/v2.1/catalog/datasets/emplacement-des-gares-idf/exports/geojson?lang=fr&timezone=Europe%2FBerlin"
# Téléchargement du contenu du fichier
response = requests.get(url)

# Vérification de la réponse
if response.status_code == 200:
    # Lecture du contenu en utilisant StringIO pour traiter les données en mémoire
    data = io.StringIO(response.content.decode('utf-8'))
    
    # Charger les données CSV dans GeoPandas
    gdf = gpd.read_file(data, delimiter=';')

    # Afficher les premières lignes du DataFrame pour vérifier que les données sont correctement chargées
    print(gdf.head())

    # Création d'une carte
    fig, ax = plt.subplots(figsize=(10, 10))

    # Affichage des données géographiques sur la carte
    gdf.plot(ax=ax, marker='o', color='red', markersize=50, label='Stations de métro')

    # Ajout d'une légende et d'un titre
    plt.legend()
    plt.title('Carte des stations de métro')

    # Affichage de la carte
    plt.show()
else:
    print("Échec du téléchargement du fichier.")

