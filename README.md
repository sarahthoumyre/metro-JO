# La voie vers les Jeux : Anticiper l'afflux dans les stations de métro pour Paris 2024

Les Jeux Olympiques de Paris 2024 éveillent l'enthousiasme avec des promesses ambitieuses mais aussi des défis cruciaux, en particulier dans le domaine de la mobilité. Les attentes sont élevées, portées par la volonté de garantir des déplacements fluides, durables et sécurisés pour tous. Néanmoins, les retards dans la réalisation du projet du Grand Paris Express et l'absence de gratuité des tickets de métro pendant cette période ont mis en évidence des défis majeurs à relever pour la région Île-de-France.

## Notre projet python 
Notre étude se concentre sur une approche idéale, un exercice de prospective visant à explorer comment, même en laissant de côté les imprévus qui ont déjà mis en évidence des difficultés dans la tenue des promesses, les transports en métro pourraient idéalement se dérouler pendant les Jeux Olympiques de Paris 2024. Notre objectif est d'imaginer un scénario optimal où tous les engagements initiaux seraient respectés. 
Cette analyse nous permettrait de visualiser une situation où le système de transport en commun serait fiable et suffisamment robuste pour acheminer 100% des spectateurs vers leurs destinations sans accroc majeur. 
Nous espérons offrir une vision prospective, une sorte de "plan de rêve" pour la mobilité à Paris pendant les Jeux Olympiques, même si la réalité actuelle semble plus complexe et moins favorable. Cela pourrait servir de référence pour comprendre les écarts entre l'idéal et les défis actuels, et peut-être proposer des recommandations pour améliorer le système de transport en prévision d'événements futurs d'envergure à Paris.
Dans ce cadre, notre approche repose sur des scénarios dynamiques spécifiques.

## Notre problématique 
Dans un monde idéal où la région Île-de-France honore ses promesses, permettant à tous d'emprunter le métro, quelles sont les prévisions d’affluences sur chaque ligne de métro et dans chaque station entre le 24 juillet 2024 et le 11 août 2024 ? 

## Nos hypothèses 
- 	**Destination : les compétitions**  \
  Nous examinons spécifiquement les flux de déplacements vers les sites des compétitions à Paris (ainsi que vers le Stade de France en Seine-Saint-Denis), éléments essentiels de l'événement.
- 	**Métro à pleine capacité** \
  Nous partons du principe que chaque participant utilisera le métro dès que possible, formant ainsi une dynamique de déplacement massive.
- 	**Suivre les conseils officiels des JO** \
  Les déplacements seront planifiés en harmonie avec les recommandations officielles des Jeux, couvrant les heures d'arrivée recommandées (il est recommandé d’arriver 1H30 avant chaque compétition https://www.paris2024.org/fr/faq/combien-de-temps-avant-le-debut-dune-session-dois-je-arriver-sur-le-site-de-competition/ ) et les lignes de métro à privilégier (les lignes de métro recommandées sont disponibles sur le site https://www.paris2024.org/ ; par exemple pour le site Arena Champ de Mars https://www.paris2024.org/fr/site/arena-champ-de-mars/)
-  **Focus sur l'anticipation, exclusion de l'inattendu** \
  Nous focalisons notre étude sur les prévisions sans considérer les incidents inattendus sur les lignes de métro, afin de visualiser un scénario optimiste.

## Notre programme de prédiction d'affluence
Notre objectif est de concevoir un programme qui, à partir de données telles que l'horaire, la date, la ligne spécifique du métro, et la station sélectionnée, sera en mesure de fournir des estimations d'affluence à la fois pour l'ensemble de la ligne de métro choisie et pour la station spécifiée à ce moment précis. Après cela, notre intention est d'illustrer nos résultats de prédiction à l'aide de statistiques descriptives. /

## Récapitulatif des fichiers présents sur notre Github

### Données importées
- Dans le dossier Données importées :
* 2022_S2_NB_FER.csv
* 2022_S2_NB_FER.csv

### Données nettoyées 
- ***Calendrier*** /
Ce jeu de données présente le calendrier complet des compétitions pendant les Jeux Olympiques. Issu du web scraping d'un calendrier en ligne, il a été traité pour convertir les dates et heures en format de date et d'heure Python afin de les rendre utilisables. Le tableau a été divisé en deux : un pour les heures de début et un pour les heures de fin. En tenant compte des indications de l'organisation des JO, une réduction de 1h30 a été appliquée à chaque heure de début, et 30 minutes ont été ajoutées à l'heure de fin pour prendre en compte le temps de départ des lieux. Ces heures ont ensuite été converties en plages horaires pour une meilleure utilisation dans le programme. On conserve uniquement les lieux à Paris et le Stade de France. 
- ***Données stations de métro 2022*** /
Ces données historiques représentent les informations sur les stations de métro pendant la période des JO en 2022, offrant ainsi une vision historique des services et de la disponibilité des stations à cette époque. Elles servent de référence pour analyser les schémas de trafic et de mouvement des voyageurs pendant les Jeux Olympiques.

- ***Informations lieux des compétitions*** / 
Ces données sont issues du web scraping et fournissent des détails importants sur les différents lieux où se déroulent les événements olympiques. Elles comprennent des informations telles que les adresses, les capacités d'accueil, les descriptions des infrastructures et d'autres détails pertinents permettant de mieux comprendre chaque site olympique. Les lieux des compétitions non desservies par les métros sont retirés de notre étude. 

- ***Informations lignes métro*** /
Ce jeu de données contient des détails spécifiques sur les lignes de métro concernées pendant la période des Jeux Olympiques. Ces informations peuvent inclure les horaires de fonctionnement, les fréquences, les arrêts desservis, les connexions et autres détails opérationnels pour faciliter les déplacements des participants et des spectateurs vers les différents sites olympiques.
  
- Programmes :
- Statistiques descriptives : 

## Packages nécessaires
- Java : Non installable via pip, mais nécessaire pour tabula-py.
- tabula-py : Utilisé pour extraire des données de fichiers PDF au format tabulaire.
- openpyxl : Utilisé pour lire et écrire des fichiers Excel au format xlsx.
- pandas : Bibliothèque de manipulation et d'analyse de données.
- numpy : Bibliothèque pour le calcul numérique.
- geopandas : Utilisé pour manipuler des données géospatiales.
- requests : Pour effectuer des requêtes HTTP.
- io : Module pour gérer les flux d'entrée/sortie.
- matplotlib.pyplot : Utilisé pour créer des visualisations.
- re : Module pour les expressions régulières.
- bs4 (BeautifulSoup) : Bibliothèque pour le scraping web.
- difflib : Module pour calculer les différences entre des chaînes de caractères.
- IPython.utils : Module IPython pour les fonctionnalités utilitaires.
- display : Pour afficher des objets IPython./
On utilise %pip install <nom_du_package> pour installer les packages dans une cellule de notebook. 

