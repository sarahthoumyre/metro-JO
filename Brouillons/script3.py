import pandas as pd
import tabula

# Lien vers le PDF contenant le tableau
lien_pdf = "https://medias.paris2024.org/uploads/2022/07/Calendrier-par-epreuves-des-Jeux-Olympiques-de-Paris-2024.pdf"

try:
    # Utilisation de tabula pour extraire le tableau du PDF
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

    # Réinitialiser l'index
    df.reset_index(drop=True, inplace=True)

    # Créer un vecteur pour l'index
    vecteur = [
        'Stade Tour Eiffel', 'Arena Champ-de-Mars', 'Grand Palais', 'Invalides', 'Hôtel de Ville',
        'Pont Alexandre III', 'Pont Iéna', 'La Concorde', 'Stade Rolland-Garros', 'Arena Paris Sud',
        'Arena Bercy', 'Arena Porte de la Chapelle', 'Paris la Défense Arena', 'Centre aquatique',
        'Stade de France', 'Site escalade du Bourget', 'Arena Paris Nord', 'Valeur par défaut'
    ]

    # Assigner le vecteur en tant qu'index du DataFrame
    df.index = vecteur

    # Afficher le DataFrame obtenu
    print(df)

except Exception as e:
    print("Une erreur s'est produite :", str(e))
