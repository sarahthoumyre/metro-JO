import pandas as pd
import tabula

# Lien vers le PDF contenant le tableau
lien_pdf = "https://medias.paris2024.org/uploads/2022/07/Calendrier-par-epreuves-des-Jeux-Olympiques-de-Paris-2024.pdf"

# Utilisation de tabula pour extraire le tableau du PDF
try:
    # Utilisation de l'option 'pages' pour spécifier la page ou les pages contenant le tableau
    df_list = tabula.read_pdf(lien_pdf, pages=[1, 2], stream=True)  # Adapter les options selon vos besoins

    # Concaténer les DataFrames obtenus des différentes pages en un seul DataFrame
    df = pd.concat(df_list)

    # Supprimer les 28 dernières lignes
    df = df.iloc[:-32]

    # Supprimer la première ligne du DataFrame
    df = df.drop(df.index[[0, 2]])  # Suppression de la première ligne
    df = df.drop(df.columns[[0]], axis=1)

    # Supprimer les lignes contenant uniquement des NaN
    df = df.dropna(how='all')


vecteur = ['Stade Tour Eiffel' if i < 4 else
           'Arena Champ-de-Mars' if i < 8 else
           'Grand Palais' if i < 13 else
           'Invalides' if i < 16 else
           'Hôtel de Ville' if i < 17 else
           'Pont Alexandre III' if i < 19 else
           'Pont Iéna' if i < 21 else
           'La Concorde' if i < 32 else
           'Stade Rolland-Garros' if i < 39 else
           'Arena Paris Sud' if i < 52 else
           'Arena Bercy' if i < 62 else
           'Arena Porte de la Chapelle' if i < 67 else
           'Paris la Défense Arena' if i < 72 else
           'Centre aquatique' if i < 78 else
           'Stade de France' if i < 83 else
           'Site escalade du Bourget' if i < 85 else
           'Arena Paris Nord' if i < 89 else
           'Valeur par défaut' for i in range(73)]

data_frame.index = vecteur

    # Affichage du DataFrame obtenu
    display(df)

except Exception as e:
    print("Une erreur s'est produite :", str(e))