# %%
import pandas as pd
%config NotebookApp.iopub_data_rate_limit=100000000000.0
url = '/workspaces/metro-JO/Données importées/2022_S2_PROFIL_FER.csv'
données_validation = pd.read_csv(url, delimiter=';')
display(données_validation)

# %%
# Convertir la colonne 'pourc_validations' en float (remplacer la virgule par un point pour séparer les décimales)
données_validation['pourc_validations'] = données_validation['pourc_validations'].str.replace(',', '.').astype(float)

# Grouper par 'LIBELLE_ARRET' et 'TRNC_HORR_60', puis calculer la somme des pourc_validations pour chaque groupe
tableau_somme_pour_validations = données_validation.groupby(['LIBELLE_ARRET', 'TRNC_HORR_60'])['pourc_validations'].sum().reset_index()

# Afficher le tableau obtenu
print("Tableau avec la somme des pourc_validations pour chaque arrêt et chaque tranche horaire :")
print(tableau_somme_pour_validations)

# %%
# Mapping des tranches horaires à des heures spécifiques
tranche_horaire_to_hour = {
    '0H-1H': '00:00-01:00',
    '1H-2H': '01:00-02:00',
    '2H-3H': '02:00-03:00',
    '3H-4H': '03:00-04:00',
    '4H-5H': '04:00-05:00',
    '5H-6H': '05:00-06:00',
    '6H-7H': '06:00-07:00',
    '7H-8H': '07:00-08:00',
    '8H-9H': '08:00-09:00',
    '9H-10H': '09:00-10:00',
    '10H-11H': '10:00-11:00',
    '11H-12H': '11:00-12:00',
    '12H-13H': '12:00-13:00',
    '13H-14H': '13:00-14:00',
    '14H-15H': '14:00-15:00',
    '15H-16H': '15:00-16:00',
    '16H-17H': '16:00-17:00',
    '17H-18H': '17:00-18:00',
    '18H-19H': '18:00-19:00',
    '19H-20H': '19:00-20:00',
    '20H-21H': '20:00-21:00',
    '21H-22H': '21:00-22:00',
    '22H-23H': '22:00-23:00',
    '23H-24H': '23:00-00:00'
}

# Appliquer la conversion des tranches horaires au format heure
tableau_somme_pour_validations['TRNC_HORR_60'] = tableau_somme_pour_validations['TRNC_HORR_60'].map(tranche_horaire_to_hour)

# Afficher le tableau avec les tranches horaires converties en heures
print("Tableau avec les tranches horaires converties au format heure :")
print(tableau_somme_pour_validations)

# %%
# Regroupement des données en cas de doublons pour une paire 'LIBELLE_ARRET'-'TRNC_HORR_60'
grouped_data = données_validation.groupby(['LIBELLE_ARRET', 'TRNC_HORR_60'])['pourc_validations'].sum().reset_index()

# Pivotement des données
pivot_table = grouped_data.pivot(index='LIBELLE_ARRET', columns='TRNC_HORR_60', values='pourc_validations').reset_index()

# Renommage des colonnes
pivot_table.columns.name = None  # Supprimer le nom de la colonne index
pivot_table = pivot_table.rename(columns=lambda x: f"{x}" if x != 'LIBELLE_ARRET' else x)

# Affichage du tableau pivoté
print("Tableau pivoté avec les pourcentages de validations pour chaque tranche horaire par LIBELLE_ARRET :")
print(pivot_table)

# %%
import re

# Sélectionner les colonnes correspondant aux tranches horaires
horaire_columns = pivot_table.columns[1:]  # Exclure la colonne 'LIBELLE_ARRET'

# Fonction pour extraire l'heure de début de chaque tranche horaire
def extract_start_hour(column):
    match = re.match(r'(\d+)H-(\d+)H', column)
    if match:
        return int(match.group(1))
    return 0

# Trier les colonnes dans l'ordre croissant des heures de début des tranches
sorted_columns = sorted(horaire_columns, key=extract_start_hour)

# Réorganiser le tableau pivoté avec les colonnes dans l'ordre chronologique
new_column_order = ['LIBELLE_ARRET'] + sorted_columns
pivot_table = pivot_table[new_column_order]

# Afficher le tableau pivoté avec les colonnes triées par tranches horaires
print("Tableau pivoté avec les colonnes triées par tranches horaires :")
print(pivot_table)

# %%
# Supprimer la colonne 'ND' du DataFrame pivot_table_ordered
pivot_table.drop(columns=['ND'], inplace=True, errors='ignore')

pivot_table['LIBELLE_ARRET'] = pivot_table['LIBELLE_ARRET'].str.lower().str.strip()

# Afficher le DataFrame après suppression de la colonne 'ND'
print("Tableau pivoté après suppression de la colonne 'ND' :")
print(pivot_table)

# %% [markdown]
# Création d'un dictionnaire contenant les fréquentations de chaque station de chaque ligne

# %%
import pandas as pd
import numpy as np

tableau_fréquentation = pd.read_excel('https://data.ratp.fr/api/explore/v2.1/catalog/datasets/trafic-annuel-entrant-par-station-du-reseau-ferre-2021/exports/xlsx?lang=fr&timezone=Europe%2FBerlin&use_labels=true')

print(tableau_fréquentation)


# %%
tableau_fréquentation = tableau_fréquentation[tableau_fréquentation['Réseau'] == 'Métro']
display(tableau_fréquentation)

# %%
colonnes_a_supprimer = ['Réseau', 'Ville', 'Arrondissement pour Paris']

tableau_fréquentation = tableau_fréquentation.drop(colonnes_a_supprimer, axis=1)

# Afficher le DataFrame après suppression des colonnes
print(tableau_fréquentation)

# %%
# Liste des colonnes à modifier
colonnes_correspondance = ['Correspondance_1', 'Correspondance_2', 'Correspondance_3', 'Correspondance_4', 'Correspondance_5']

# Convertir les colonnes spécifiées en type chaîne (si elles ne le sont pas déjà)
tableau_fréquentation[colonnes_correspondance] = tableau_fréquentation[colonnes_correspondance].astype(str)

# Supprimer les lettres 'A' et 'B' des colonnes spécifiées dans tableau_fréquentation
for colonne in colonnes_correspondance:
    tableau_fréquentation[colonne] = tableau_fréquentation[colonne].str.replace('A', '').str.replace('B', '')

# Afficher le DataFrame après suppression des lettres spécifiées
print(tableau_fréquentation)

# %%
# Liste des colonnes à modifier
colonnes_correspondance = ['Correspondance_1', 'Correspondance_2', 'Correspondance_3', 'Correspondance_4', 'Correspondance_5']

# Remplacer "nan" par "NaN" dans les colonnes spécifiées
tableau_fréquentation[colonnes_correspondance] = tableau_fréquentation[colonnes_correspondance].replace('nan', 'NaN')

# Afficher le DataFrame avec les remplacements effectués
print(tableau_fréquentation)

# %%
# Liste des colonnes à analyser
colonnes_correspondance = ['Correspondance_1', 'Correspondance_2', 'Correspondance_3', 'Correspondance_4', 'Correspondance_5']

# Calcul du nombre de cases non vides pour chaque ligne
tableau_fréquentation['nb_correspondance'] = tableau_fréquentation[colonnes_correspondance].count(axis=1)

# Afficher le DataFrame avec la nouvelle colonne "nb_correspondance"
print(tableau_fréquentation)

# %%
# Diviser les valeurs de la colonne "Trafic" par les valeurs de la colonne "nb_correspondance"
tableau_fréquentation['Trafic'] = tableau_fréquentation['Trafic'] / tableau_fréquentation['nb_correspondance']

# Afficher le DataFrame avec les valeurs mises à jour
print(tableau_fréquentation)

# %%
#Nettoyage de données sur le nombre de validations: on obtient le nombre de validation moyen par jour sur 1 mois précis

import pandas as pd
%config NotebookApp.iopub_data_rate_limit=100000000000.0
url2 = '/workspaces/metro-JO/Données importées/2022_S2_NB_FER.csv'
données_validation2= pd.read_csv(url2)
données_validation2 = pd.read_csv(url2, delimiter=';')

# Exemple avec gestion de formats flexibles
données_validation2['JOUR'] = pd.to_datetime(données_validation2['JOUR'], errors='coerce', format="%d/%m/%Y")
donnees_mai = données_validation2.loc[(données_validation2['JOUR'].dt.month == 5)]
donnees_sum = donnees_mai.groupby('LIBELLE_ARRET')['NB_VALD'].mean().reset_index()

# Conversion de la colonne 'JOUR' en datetime
données_validation2['JOUR'] = pd.to_datetime(données_validation2['JOUR'], format='%d/%m/%Y')

# Filtrer les données pour les dates spécifiques
donnees_filtrees = données_validation2[(données_validation2['JOUR'] >= '2022-07-24') & (données_validation2['JOUR'] <= '2022-08-11')]

# Grouper par 'JOUR', 'LIBELLE_ARRET' et 'CATEGORIE_TITRE' et calculer la somme des 'NB_VALD'
donnees_aggreg = donnees_filtrees.groupby(['JOUR', 'LIBELLE_ARRET', 'CATEGORIE_TITRE'])['NB_VALD'].sum().reset_index()

# Conversion de la colonne 'JOUR' en datetime si ce n'est pas déjà fait
données_validation2['JOUR'] = pd.to_datetime(données_validation2['JOUR'], format='%d/%m/%Y')

# Filtrage des dates spécifiques
donnees_filtrees = données_validation2[(données_validation2['JOUR'] >= '2022-07-24') & (données_validation2['JOUR'] <= '2022-08-11')]

# Somme de NB_VALD par JOUR et par LIBELLE_ARRET
somme_par_jour_arret = donnees_filtrees.groupby(['JOUR', 'LIBELLE_ARRET'])['NB_VALD'].sum().reset_index()

moyenne_par_arret = somme_par_jour_arret.groupby('LIBELLE_ARRET')['NB_VALD'].mean().reset_index()

# Normalisation des libellés
moyenne_par_arret['LIBELLE_ARRET'] = moyenne_par_arret['LIBELLE_ARRET'].str.lower().str.strip()

# Somme des valeurs de NB_VALD pour les libellés normalisés
moyenne_par_arret = moyenne_par_arret.groupby('LIBELLE_ARRET')['NB_VALD'].sum().reset_index()

# Suppression des doublons
moyenne_par_arret = moyenne_par_arret.drop_duplicates(subset=['LIBELLE_ARRET'])

display(somme_par_jour_arret)
display(moyenne_par_arret)

# %%
import pandas as pd

# Vos données et numéro
# Assumons que vous avez déjà vos données dans un DataFrame nommé tableau_fréquentation
numéro = [1, 2, 3, '3bis', 4, 5, 6, 7, '7bis', 8, 9, 10, 11, 12, 13, 14]

# Création des tableaux pour chaque élément de numéro
tableaux = {}

colonnes_correspondance = ['Correspondance_1', 'Correspondance_2', 'Correspondance_3', 'Correspondance_4', 'Correspondance_5']

for k in numéro:
    # Convertir k en string car il peut contenir des valeurs non numériques
    k_str = str(k)
    
    # Filtrer les lignes où la valeur k est présente dans les colonnes spécifiées
    filtered_rows = tableau_fréquentation[tableau_fréquentation[colonnes_correspondance].apply(lambda x: k_str in x.values, axis=1)]
    
    # Stocker les lignes filtrées dans un tableau nommé "ligne numéro[k]"
    tableaux[f'ligne numéro[{k_str}]'] = filtered_rows

# Parcourir chaque tableau dans le dictionnaire et supprimer les colonnes spécifiées
for tableau_nom, tableau in tableaux.items():
    tableaux[tableau_nom] = tableau.drop(columns=colonnes_correspondance)

# Parcourir chaque tableau dans le dictionnaire
for tableau_nom, tableau in tableaux.items():
    # Calculer la fréquentation totale pour chaque tableau
    fréquentation_totale_ligne = tableau['Trafic'].sum()

    # Ajouter la variable fréquentation_totale à chaque tableau
    tableaux[tableau_nom]['fréquentation_totale_ligne'] = fréquentation_totale_ligne
    tableau['Trafic_divisé'] = tableau['Trafic'] / tableau['fréquentation_totale_ligne']

# Supposons que la clé pour la correspondance soit 'LIBELLE_ARRET' dans le tableau moyenne_par_arret
cle_correspondance = 'LIBELLE_ARRET'

# Nettoyage des espaces et uniformisation de la casse
moyenne_par_arret['LIBELLE_ARRET'] = moyenne_par_arret['LIBELLE_ARRET'].str.strip().str.lower()
for tableau_nom, tableau in tableaux.items():
    tableau['Station'] = tableau['Station'].str.strip().str.lower()

    # Fusion en utilisant les noms de stations nettoyés
    merged_table = pd.merge(tableau, moyenne_par_arret, left_on='Station', right_on='LIBELLE_ARRET', how='left')
    
    # Renommer la colonne NB_VALD de moyenne_par_arret
    merged_table = merged_table.rename(columns={'NB_VALD': 'fréquentation moyenne hors JO'})
    
    tableaux[tableau_nom] = merged_table

# %% [markdown]
# Compléter avec les valeurs manquantes

# %%
import difflib

# Méthode pour trouver la correspondance la plus proche
def find_closest_match(target, candidates):
    closest_match = difflib.get_close_matches(target, candidates, n=1, cutoff=0.6)  # Ajustez le seuil selon vos besoins
    return closest_match[0] if closest_match else None

for k in numéro:
    k_str = str(k)
    # Accéder aux tableaux spécifiques
    current_table = tableaux[f'ligne numéro[{k_str}]']
    
    # Filtrer les lignes avec des valeurs manquantes dans la colonne 'LIBELLE_ARRET'
    missing_data = current_table[current_table['LIBELLE_ARRET'].isnull()]
    
    # Remplir les valeurs manquantes
    for index, row in missing_data.iterrows():
        closest_match = find_closest_match(row['Station'], moyenne_par_arret['LIBELLE_ARRET'])
        
        if closest_match:
            tableaux[f'ligne numéro[{k_str}]'].at[index, 'LIBELLE_ARRET'] = closest_match



# %%
for k in numéro:
    k_str = str(k)
    # Accéder à chaque tableau spécifique
    current_table = tableaux[f'ligne numéro[{k_str}]']

    # Fusionner avec le tableau moyenne_par_arret pour obtenir les valeurs NB_VALD associées
    merged_with_nb_vald = pd.merge(current_table, moyenne_par_arret[['LIBELLE_ARRET', 'NB_VALD']],
                                   left_on='LIBELLE_ARRET', right_on='LIBELLE_ARRET', how='left')
    
    # Renommer la colonne NB_VALD pour plus de clarté
    merged_with_nb_vald = merged_with_nb_vald.rename(columns={'NB_VALD': 'moyenne_NB_VALD_hebdo_période_jo_2022_dans_toute_la_station'})

    # Mettre à jour le tableau dans le dictionnaire
    tableaux[f'ligne numéro[{k_str}]'] = merged_with_nb_vald

for k in numéro:
    k_str = str(k)
    # Accéder à chaque tableau spécifique
    current_table = tableaux[f'ligne numéro[{k_str}]']

    # Fusionner les données avec le tableau contenant les nouvelles colonnes
    merged_table = pd.merge(current_table, pivot_table, on='LIBELLE_ARRET', how='left')

    # Afficher le tableau fusionné pour vérification
    print(f"Tableau fusionné pour 'ligne numéro[{k_str}]':")
    display(merged_table)

    # Mettre à jour le tableau dans le dictionnaire avec les nouvelles colonnes fusionnées
    tableaux[f'ligne numéro[{k_str}]'] = merged_table

# %%
for k in numéro:
    k_str = str(k)
    # Accéder à chaque tableau spécifique
    current_table = tableaux[f'ligne numéro[{k_str}]']

    # Supprimer les colonnes 'fréquentation moyenne hors JO' et 'LIBELLE_ARRET' si elles existent
    columns_to_drop = ['fréquentation moyenne hors JO', 'LIBELLE_ARRET']
    current_table = current_table.drop(columns=columns_to_drop, errors='ignore')

    # Mettre à jour le tableau dans le dictionnaire
    tableaux[f'ligne numéro[{k_str}]'] = current_table

    # Afficher le tableau mis à jour
    print(f"Tableau 'ligne numéro[{k_str}]' après remplissage:")
    display(tableaux[f'ligne numéro[{k_str}]'])


# %%

for k in numéro:
    k_str = str(k)
    # Accéder à chaque tableau spécifique
    current_table = tableaux[f'ligne numéro[{k_str}]']

    # Colonnes à supprimer
    columns_to_drop = ['Trafic', 'fréquentation_totale_ligne', 'Trafic_divisé']

    # Vérifier si les colonnes existent avant de les supprimer
    columns_exist = [col for col in columns_to_drop if col in current_table.columns]

    # Supprimer les colonnes existantes
    if columns_exist:
        current_table = current_table.drop(columns=columns_exist)

    # Mettre à jour le tableau dans le dictionnaire
    tableaux[f'ligne numéro[{k_str}]'] = current_table

    # Afficher le tableau mis à jour
    print(f"Tableau 'ligne numéro[{k_str}]' sans les colonnes 'Trafic', 'fréquentation_totale_ligne', 'Trafic_divisé' :")
    display(tableaux[f'ligne numéro[{k_str}]'])


# %%
for k in numéro:
    k_str = str(k)
    # Accéder à chaque tableau spécifique
    current_table = tableaux[f'ligne numéro[{k_str}]']

    # Vérifier si les colonnes existent avant de créer la nouvelle colonne
    if 'moyenne_NB_VALD_hebdo_période_jo_2022_dans_toute_la_station' in current_table.columns and 'nb_correspondance' in current_table.columns:
        # Calcul de la nouvelle colonne
        current_table['moyenne_NB_VALD_hebdo_période_jo_2022_par_ligne'] = current_table['moyenne_NB_VALD_hebdo_période_jo_2022_dans_toute_la_station'] / current_table['nb_correspondance']

        # Mettre à jour le tableau dans le dictionnaire
        tableaux[f'ligne numéro[{k_str}]'] = current_table

for k in numéro:
    k_str = str(k)
    # Accéder à chaque tableau spécifique
    current_table = tableaux[f'ligne numéro[{k_str}]']

    # Vérifier si les colonnes existent avant de créer la nouvelle colonne
    if 'moyenne_NB_VALD_hebdo_période_jo_2022_dans_toute_la_station' in current_table.columns and 'nb_correspondance' in current_table.columns:
        # Calcul de la nouvelle colonne
        current_table['moyenne_NB_VALD_hebdo_période_jo_2022_par_ligne_par_direction'] = current_table['moyenne_NB_VALD_hebdo_période_jo_2022_dans_toute_la_station'] / current_table['nb_correspondance'] / 2

        # Mettre à jour le tableau dans le dictionnaire
        tableaux[f'ligne numéro[{k_str}]'] = current_table

for k in numéro:
    k_str = str(k)
    # Accéder à chaque tableau spécifique
    current_table = tableaux[f'ligne numéro[{k_str}]']

    # Vérifier si la colonne existe avant de créer la nouvelle colonne
    if 'moyenne_NB_VALD_hebdo_période_jo_2022_par_ligne' in current_table.columns:
        # Calculer la somme de la colonne spécifique
        current_table['nombre_validations_totales_pour_la_ligne'] = current_table['moyenne_NB_VALD_hebdo_période_jo_2022_par_ligne'].sum()

        # Mettre à jour le tableau dans le dictionnaire
        tableaux[f'ligne numéro[{k_str}]'] = current_table
        # Afficher le tableau mis à jour
        print(f"Tableau 'ligne numéro[{k_str}]' avec la nouvelle colonne 'moyenne_NB_VALD_hebdo_période_jo_2022_par_ligne_par_direction' :")
        display(tableaux[f'ligne numéro[{k_str}]'])



