# La voie vers les Jeux : Anticiper l'afflux dans les stations de métro pour Paris 2024

Les Jeux Olympiques de Paris 2024 éveillent l'enthousiasme avec des promesses ambitieuses mais aussi des défis cruciaux, en particulier dans le domaine de la mobilité. Les attentes sont élevées, portées par la volonté de garantir des déplacements fluides, durables et sécurisés pour tous. Néanmoins, les retards dans la réalisation du projet du Grand Paris Express et l'absence de gratuité des tickets de métro pendant cette période ont mis en évidence des défis majeurs à relever pour la région Île-de-France.

## Notre projet 
Notre étude se concentre sur un exercice de prospective visant à explorer comment, en laissant de côté les imprévus qui ont déjà mis en évidence des difficultés dans la tenue des promesses, les transports en métro pourraient idéalement se dérouler pendant les Jeux Olympiques de Paris 2024. Notre objectif est d'imaginer un scénario optimal où tous les engagements initiaux seraient respectés. 

Cette analyse nous permettrait de visualiser une situation où le système de transport en commun serait fiable et suffisamment robuste pour acheminer 100% des spectateurs vers leurs destinations sans accroc majeur. 

Nous espérons offrir une vision prospective, une sorte de "plan de rêve" pour la mobilité à Paris pendant les Jeux Olympiques, même si la réalité actuelle semble plus complexe et moins favorable. Cela pourrait servir de référence pour comprendre les écarts entre l'idéal et les défis actuels, et peut-être proposer des recommandations pour améliorer le système de transport en prévision d'événements futurs d'envergure à Paris.

## Notre problématique 
Dans un monde idéal où la région Île-de-France honore ses promesses, permettant à tous d'emprunter le métro, quelles sont les prévisions d’affluences sur chaque ligne de métro et dans chaque station entre le 24 juillet et le 11 août 2024 ? 

## Nos hypothèses 
- 	**Destination : les compétitions**  \
  Nous examinons spécifiquement les flux de déplacements vers les sites des compétitions à Paris (ainsi que vers le Stade de France en Seine-Saint-Denis), éléments essentiels de l'événement.
- 	**Métro à pleine capacité** \
  Nous partons du principe que chaque participant utilisera le métro dès que possible, formant ainsi une dynamique de déplacement massive.
- 	**Suivre les conseils officiels des JO** \
  Les déplacements seront planifiés en harmonie avec les recommandations officielles des Jeux, couvrant les heures d'arrivée recommandées (il est recommandé d’arriver 1H30 avant chaque compétition ; source : https://www.paris2024.org/fr/faq/combien-de-temps-avant-le-debut-dune-session-dois-je-arriver-sur-le-site-de-competition/) et les lignes de métro à privilégier (les lignes de métro recommandées sont disponibles sur le site https://www.paris2024.org/)
-  **Focus sur l'anticipation, exclusion de l'inattendu** \
  Nous focalisons notre étude sur les prévisions sans considérer les incidents inattendus sur les lignes de métro, afin de visualiser un scénario optimiste.

## Notre programme de prédiction d'affluence
Notre objectif est de concevoir un programme qui, à partir de données (horaire, date, ligne spécifique du métro, station sélectionnée) sera en mesure de fournir des estimations d'affluence à la fois pour l'ensemble de la ligne de métro choisie et pour la station spécifiée à ce moment précis. Après cela, notre intention est d'illustrer nos résultats de prédiction à l'aide de statistiques descriptives. Ces résultats sont disponibles sur le notebook Main.

## Récapitulatif des fichiers présents sur notre Github

### A. Données importées
On trouve dans le dossier Données importées deux jeux de données disponibles sur le site https://www.data.gouv.fr/fr/datasets/historique-des-donnees-de-validation-sur-le-reseau-ferre-2015-2022/. Nous utilisons les jeux de données du deuxième semestre de l'année 2022 pour nos données historiques. Ces fichiers ne sont pas directement accessibles via les liens de téléchargement, car le fichier zip contient des fichiers pour différentes années. C'est pourquoi nous les avons mis à disposition sur notre GitHub.
* **2022_S2_NB_FER.csv** \
Ce jeu de données présente le nombre de validations des voyageurs par jour par arrêt et par titre de transport sur le réseau ferré.
* **2022_S2_PROFIL_FER.csv** \
Ce jeu de données présente les profils horaires des validations des voyageurs par jour type et par arrêt sur le réseau ferré.

### B. Données nettoyées 

1. **Informations lieux des compétitions** 
   
Ce notebook est destiné à collecter des informations sur les lieux des compétitions pour les Jeux Olympiques de Paris 2024 à partir du site officiel de l'événement ainsi que d'autres sources en ligne, et à organiser ces données dans un tableau. \
L'objectif final est d'avoir un tableau organisé contenant des informations sur les lieux des compétitions, y compris la capacité, les arrêts de métro à proximité, les lignes de métro et le nombre de personnes attendues pour chaque événement.

  **Hypothèses** :
  - Les informations sur les lieux des compétitions sont disponibles sur le site officiel de Paris 2024 (https://www.paris2024.org). 
  - Les noms des lieux de compétition ont été fournis sous forme de liste appelée lieux. Les URLs des pages spécifiques pour chaque lieu ont été générées à partir des noms de lieux fournis.
  - Les informations sur les arrêts de métro à proximité et les lignes de métro associées à chaque lieu de compétition peuvent être extraites des pages web spécifiques.
  - Certaines données manquantes sont obtenues à partir d'autres sources pertinentes comme des articles de presse ou des sites tiers (pour la Concorde : https://sportetsociete.org/2022/10/20/paris-2024-un-cadre-majestueux-pour-louverture-des-jeux-paralympiques ; pour Arena Paris Sud : https://fr.wikipedia.org/wiki/Arena_Porte_de_la_Chapelle).

  **Packages nécessaires** :
  - Pandas pour la manipulation de données tabulaires.
  - Requests pour effectuer des requêtes HTTP vers les sites web.
  - BeautifulSoup (module bs4) pour analyser et extraire des informations à partir du HTML des pages web.
  - Re pour les expressions régulières.

2. **Calendrier**  

  Ce notebook effectue un webscraping du calendrier des compétitions pour les Jeux Olympiques de Paris 2024 à partir d'un fichier PDF hébergé sur le site de Paris 2024. Le script assure la récupération des données du calendrier des compétitions, leur structuration et la préparation pour une utilisation plus aisée dans l'analyse et la visualisation des    horaires et des lieux des compétitions pour les Jeux Olympiques de Paris 2024. Le tableau a été divisé en deux parties distinctes : l'une pour les heures de début des événements et l'autre pour les heures de fin. L'objectif de cette division était de traiter ces données pour les rendre plus adaptées à une utilisation pratique dans nos programmes.

  **Hypothèses** :
  - Les informations sur le calendrier des compétitions sont disponibles dans un PDF spécifique hébergé à l'adresse fournie (https://medias.paris2024.org/uploads/2022/07/Calendrier-par-epreuves-des-Jeux-Olympiques-de-Paris-2024.pdf)
  - Les lieux de compétition sont déjà connus et sont listés dans le vecteur lieux.
  - Pour s'aligner avec les directives et les indications spécifiques de l'organisation des Jeux Olympiques, une réduction de 1h30 a été appliquée à chaque heure de début des       événements. Cette réduction prend en compte le temps nécessaire pour permettre aux participants et aux spectateurs de se rendre sur les lieux des compétitions.
  - De manière similaire, 30 minutes ont été ajoutées à l'heure de fin de chaque événement pour prendre en compte le temps de départ des lieux une fois les compétitions terminées.
  - Les heures ainsi ajustées ont ensuite été converties en plages horaires, créant des intervalles de temps spécifiques pour chaque événement.
  - Seuls les lieux à Paris ainsi que le Stade de France ont été conservés dans ce jeu de données. Cette sélection a été effectuée en fonction des lieux accessibles par métro      (identifiés dans le notebook Informations lieux des compétitions).

  **Packages nécessaires** :
  - Pandas pour la manipulation de données tabulaires.
  - Java nécessaire pour tabula-py.
  - Tabula pour extraire les données à partir d'un fichier PDF.
  - NumPy pour certaines opérations de manipulation de données.

3. **Données stations de métro 2022**
   
  Ce script utilise la bibliothèque Pandas pour importer, analyser et manipuler des données relatives aux validations des voyageurs dans le réseau ferré pendant le second           semestre de l'année 2022. Il effectue différentes opérations sur ces données, provenant de sources variées comme des fichiers CSV accessibles localement (dans le     dossier Données importées). Ces données historiques représentent une référence pour analyser les schémas de trafic, la fréquentation des stations de métro et les tendances de     validation des voyageurs. Des opérations de filtrage sont effectuées pour obtenir les données spécifiques à la période des Jeux Olympiques, mais en 2022 (c'est-à-dire du 24       juillet au 11 août 2022). Ces données filtrées sont agrégées et des calculs de moyennes sont réalisés pour obtenir le nombre moyen de validations par arrêt sur cette période.

   **Packages nécessaires** :
  - Pandas pour la manipulation et l'analyse des données tabulaires.
  - re pour travailler avec les expressions régulières dans la manipulation des chaînes de caractères.

4. **Informations lignes métro**
   
  Ce notebook contient des détails spécifiques sur les lignes de métro concernées pendant la période des Jeux Olympiques. Le programme importe des données de fréquentation des      stations de métro de la RATP pour l'année 2021 (qui sont les données disponibles les plus récentes, disponibles sur le lien https://data.ratp.fr/api/explore/v2.1/catalog/datasets/trafic-annuel-entrant-par-station-du-reseau-ferre-2021/exports/xlsx?lang=fr&timezone=Europe%2FBerlin&use_labels=true), puis effectue une série de traitements pour analyser ces données. Il crée un dictionnaire de tableaux pour chaque ligne de         métro, analysant la fréquentation de chaque station (en fournissant diverses statistiques telles que la moyenne quotidienne pendant la période des JO en 2022, la part de trafic par station     etc).

  **Packages nécessaires** :
  - Pandas  pour la manipulation des données sous forme de DataFrame.
  - numpy pour des opérations mathématiques.
  - re pour les opérations liées aux expressions régulières.
  - difflib pour trouver les correspondances les plus proches entre les noms des stations.
  - io et display de IPython pour la capture de sortie et l'affichage dans un notebook.
  
### C. Main
  Le notebook main contient une copie des notebook Programmes et Statistiques descriptives.  

  1. **Programmes**
   
  **Principales fonctions** :
  - affluence_hors_jo : Calcule l'affluence à une station et à une heure spécifiques sur une ligne donnée, sans tenir compte des JO.
  - calculer_personnes_supplementaires : Calcule le nombre de personnes supplémentaires à une station et sur une ligne données en raison des JO.
  - info_trafic : Calcule le nombre total de personnes à une station et sur une ligne à une heure spécifique, prenant en compte les JO. Combine les résultats des fonctions précédentes pour obtenir l'affluence totale.
  - comparer_affluences : Compare l'affluence actuelle à une heure donnée à celle prévue pour une heure suivante. Donne des indications sur l'évolution probable du trafic en fonction de cette comparaison.
  - info_trafic_complet : Fournit des informations complètes sur l'affluence à une station et sur une ligne à une heure spécifique, en incluant les prédictions de trafic.

  **Packages nécessaires** :
  - Pandas pour la manipulation des données sous forme de tableaux.
  - tabula-py pour extraire des données de fichiers PDF sous forme de tableaux.
  - numpy pour des calculs numériques.
  - IPython pour la capture de sortie dans un notebook Jupyter.

  2. **Statistiques descriptives**  

  Nos statistiques descriptives se divisent en deux parties : une première partie réalisée à partir des données importées et nettoyées (voir ci-dessous la description de ces données) ; et une seconde partie réalisée à partir des résultats de nos programmes.

  **Packages nécessaires** :
  - Pandas pour la manipulation et l'analyse des données tabulaires.
  - NumPy pour le calcul numérique et les opérations sur les tableaux.
  - Matplotlib pour la visualisation de données avec des graphiques statiques.
  - Plotly pour la création de graphiques interactifs.
  - Seaborn pour la création de graphiques statistiques esthétiques basés sur Matplotlib.
  - Scipy pour les calculs statistiques et les tests.
  - Statsmodels pour l'estimation de modèles statistiques et l'analyse de données.
  - Tabula pour extraire les données de PDF en fichiers tabulaires. 
  - Scikit-learn pour l'apprentissage automatique et l'analyse de données prédictives.

## Bilan des packages nécessaires
- Pandas
- NumPy
- Requests
- BeautifulSoup (module bs4)
- Re
- Java (pour tabula-py)
- Tabula
- IO et Display de IPython
- Matplotlib
- Plotly
- Seaborn
- Scipy
- Statsmodels
- Difflib
- Scikit-learn.  
On utilise %pip install <nom_du_package> pour installer les packages dans une cellule de notebook. 
