import json
import requests
from datetime import datetime

# Fonctions pour récupérer automatiquement les données sur le serveur Uvicorn
# A MODIFIER SELON L'ADRESSE UTILISÉE
url = "http://127.0.0.1:8000/" 

# Récupère le statut du serveur, s'il y a des nouvelles données
def check_serv_status(db_size : int):
    response = get_data()
    serv_size = len(response)
    if serv_size > db_size:
        return f"{serv_size - db_size} new data available"

# Récupère la taille des données serveur
def get_serv_size():
    return len(get_data())

# Récupère toutes les données serveur
def get_data():
    response = requests.get(url).json()
    return response    

# Ajoute les dernières données dans le fichier log.json
# Modifier l'extension en log.txt quand j'aurai fini

def add_log_entry(new_entry : dict):
    ## Changer le path après avoir fini le setup dev
    json_file = open("log.json", "r")
    log = json.load(json_file)
    json_file.close()
    log.update({int(datetime.now().timestamp()):new_entry})
    ## Changer le path après avoir fini le setup dev
    file = open("log.json","w")
    json.dump(log,file, indent=6)
    file.close()
