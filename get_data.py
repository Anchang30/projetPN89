import json
import requests
from datetime import datetime

# Functions to get informations from Uvicorn server
#### A MODIFIER SELON L'ADRESSE UTILISÉE
url = "http://127.0.0.1:8000/" 

# Gets server size to remember where to continue parsing
def get_serv_size():
    return len(get_data())

# Gets server status if new data available
def check_serv_status(db_size : int):
    serv_size = get_serv_size()
    if serv_size > db_size:
        return f"{serv_size - db_size} new data available"

# Gets all data from server
def get_data():
    return requests.get(url).json()

# Adds new data as entry in the JSON logfile
#### Modifier l'extension en log.txt quand j'aurai fini
def add_log_entry(new_entry : dict, log_name :str):
    json_file = open(log_name, "r")
    log = json.load(json_file)
    json_file.close()
    log.update({int(datetime.now().timestamp()):new_entry})
    file = open(log_name,"w")
    json.dump(log,file, indent=6)
    file.close()
