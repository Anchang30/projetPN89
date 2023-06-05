# projetPN89

Script Python qui va récupérer les données du passage à niveau PN89 sur la plateforme Oxygen sous forme de JSON :
    Données de sonneries d'alarme (start_time et end_time)
    Données des feux de signalisation (start_time et end_time)
    Données des barrières (start_time, start_angle, end_angle et end_time) + état de la barrière

Lors de la récupération des données, les barrières et leurs outils respectifs sont mis à jour, les données sont sauvegardées dans des fichiers log locaux (log*.txt) 

On vérifie ensuite les 3 cas d'usage suivants :
    - (1) La barrière n'est pas abaissée après 8 secondes d'allumage des feux de signalisation
    - (2) le mouvement d'une barrière dure plus de 12 secondes
    - (3) le positionnement anormal d'une barrière dure plus de 20 secondes (non vertical ou non horizontal)

La validation d'un cas d'usage génère un log d'erreur qui sera envoyé sur un elasticsearch/kibana afin de conserver les comportements erronés,
ainsi que pour réaliser des visualisations selon les types d'erreur rencontrés : no data (pas de données de la barrière), not down (1),
is slow (2), irregular (3).

/!\ Il conviendra de vérifier et de MAJ les champs suivants dans le code avant la mise en production :

        - virer le dossier dev du répo Git, ainsi que les résidus autres

        - numéros de série des différents outils (db.py : barrières, sonneries et feux de signalisation)

        - url de l'endpoint (get_data.py : déjà renseigné selon le cahier des charge)
    
        - end point de l'elasticsearch (es_management.py : qui sera dans un container donc normalement bien paramétré)

        - fenêtre temporelle de récupération des données (script.py)

        - références au dictionnaire des capteurs (normalement OK mais cross checking)

        - emplacement du dossier contenant les logs de données (actuellement situé à la racine du le package)

        - complétude du requirements.txt avant le lancement de la conteneurisation (sera normalement déjà réalisé avec le Dockerfile ou le .yaml)

        - vérifier si le rechargement du logging est nécessaire (services.py : ligne 12)