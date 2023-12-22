import pandas as pd
import tabula

lieux = ['Stade Tour Eiffel','Arena Champ-de-Mars', 'Grand Palais', 'Invalides', 'Hôtel de Ville', 'Pont Alexandre III', 'Trocadéro', 'La Concorde', 'Stade Roland-Garros', 'Arena Paris Sud', 'Arena Bercy', 'Arena Porte de la Chapelle', 'Paris la Défense Arena', 'Centre aquatique', 'Stade de France', 'Site escalade du Bourget', 'Arena Paris Nord']

vecteur = ['Stade Tour Eiffel' if i < 4 else
           'Arena Champ-de-Mars' if i < 8 else
           'Grand Palais' if i < 13 else
           'Invalides' if i < 16 else
           'Hôtel de Ville' if i < 17 else
           'Pont Alexandre III' if i < 19 else
           'Trocadéro' if i < 21 else
           'La Concorde' if i < 32 else
           'Stade Roland-Garros' if i < 38 else
           'Arena Paris Sud' if i < 51 else
           'Arena Bercy' if i < 61 else
           'Arena Porte de la Chapelle' if i < 66 else
           'Paris la Défense Arena' if i < 71 else
           'Centre aquatique' if i < 77 else
           'Stade de France' if i < 82 else
           'Site escalade du Bourget' if i < 84 else
           'Arena Paris Nord' if i < 88 else
           'Valeur par défaut' for i in range(88)]


# Lien vers le PDF contenant le tableau
lien_pdf = "https://medias.paris2024.org/uploads/2022/07/Calendrier-par-epreuves-des-Jeux-Olympiques-de-Paris-2024.pdf"

try : 
    # Utilisation de tabula pour extraire le tableau du PDF
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

    df.index = vecteur
    
    # Affichage du DataFrame obtenu
    display(df)

except Exception as e:
        print("Une erreur s'est produite :", str(e))
