import json
import requests
from datetime import datetime

# Fonctions pour récupérer automatiquement les données sur le serveur Uvicorn
# A MODIFIER SELON L'ADRESSE UTILISÉE
url = "http://127.0.0.1:8000/" 

# Récupère le statut du serveur, s'il y a des nouvelles données
def check_serv_status(db_size : int):
    serv_size = len(get_data())
    if serv_size > db_size:
        return f"{serv_size - db_size} new data available"

# Récupère la taille des données serveur
def get_serv_size():
    return len(get_data())

# Récupère toutes les données serveur
def get_data():
    return requests.get(url).json()

# Ajoute les dernières données dans le fichier log.json
# Modifier l'extension en log.txt quand j'aurai fini
def add_log_entry(new_entry : dict):
    json_file = open("log.json", "r")
    log = json.load(json_file)
    json_file.close()
    log.update({int(datetime.now().timestamp()):new_entry})
    file = open("log.json","w")
    json.dump(log,file, indent=6)
    file.close()
