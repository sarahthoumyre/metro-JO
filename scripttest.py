lieux = ['Stade Tour Eiffel','Arena Champ-de-Mars', 'Grand Palais', 'Invalides', 'Hôtel de Ville', 'Pont Alexandre III', 'Pont Iéna', 'La Concorde', 'Stade Rolland-Garros', 'Arena Paris Sud', 'Arena Bercy', 'Arena Porte de la Chapelle', 'Paris la Défense Arena', 'Centre aquatique', 'Stade de France', 'Site escalade du Bourget', 'Arena Paris Nord']

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

print(vecteur)