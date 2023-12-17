# Données
horaire_evenement = "14:00"  # Horaire de l'événement
temps_avant_evenement = 90  # Temps avant l'événement que tout le monde arrive (en minutes)
temps_marche_station = 10  # Temps de marche jusqu'à la station de la ligne 12 (en minutes)
nombre_personnes = 50000  # Nombre de personnes prenant la ligne 12 pour l'événement

# % de fréquentation de chaque station par rapport à la fréquentation totale de la ligne 12
pourcentage_frequentation = {
    "Station_A": 0.1,
    "Station_B": 0.15,
    # ... Ajoutez les pourcentages pour chaque station
    "Station_Z": 0.05
}

# Horaires de départ de métro
horaires_depart = {
    "Station_A": ["07:00", "07:30", "08:00", "08:30"],  # Exemple d'horaires de départ pour la Station A
    # ... Ajoutez les horaires pour chaque station
    "Station_Z": ["06:45", "07:15", "07:45", "08:15"]
}

# Temps de trajet pour arriver à la station finale depuis chaque station de la ligne 12
temps_trajet_vers_station_finale = {
    "Station_A": 25,
    "Station_B": 30,
    # ... Ajoutez les temps pour chaque station
    "Station_Z": 15
}

# Données
capacite_metro = 200  # Capacité du métro
personnes_attendant = 10000  # Nombre de personnes attendant le métro

def calcul_attente_metro(horaire, station):
    temps_attente = 0

    # Votre logique pour calculer le temps d'attente en fonction des données fournies
    # ... (à compléter en utilisant les données fournies)

    return temps_attente

# Horaire d'arrivée de chaque métro
horaires_arrivee_metro = [
    "08:00", "08:15", "08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15"
    # Ajoutez les horaires d'arrivée des métros suivants
]

def prochain_metro_attente(capacite, personnes_attendantes, horaires_arrivee):
    # Calcul du nombre de métros nécessaires
    nb_metros_necessaires = personnes_attendantes / capacite

    # Calcul du prochain métro disponible
    heure_actuelle = datetime.datetime.now().strftime("%H:%M")
    prochain_metro = None

    for horaire in horaires_arrivee:
        if horaire > heure_actuelle:
            prochain_metro = horaire
            break



# Utilisation du programme
horaire_entree = input("Entrez l'horaire (format HH:MM) : ")
station_entree = input("Entrez la station de la ligne 12 : ")

temps_attente = calcul_attente_metro(horaire_entree, station_entree)
print(f"Le temps d'attente estimé pour le métro à la station {station_entree} à {horaire_entree} est de {temps_attente} minutes.")

import datetime




