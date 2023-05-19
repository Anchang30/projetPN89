import json
import requests
from datetime import datetime
import os

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

# CREATES LOG FOLDER IF IT DOESNT EXIST AND RETURN THE NB OF LOG FILES IN IT
def logfile_name():
    path_ = os.getcwd()
    log_path = os.path.join(os.getcwd(), "logs")
    if "logs" not in os.listdir(path_):
        os.mkdir(log_path)
    len_json = len([doc for doc in os.listdir(log_path) if doc.startswith("log") and doc.endswith(".json")])
    if len_json == 0:
        return "log.json"
    else :
        return f"log{len_json-1}.json"

# CREATES A NEW LOGFILE FOR EACH NEW SESSION    
def create_logfile(log_name : str):
    log_path = os.path.join(os.getcwd(), "logs")
    logfile_path = os.path.join(log_path, log_name)
    print('Creating log file')
    with open(logfile_path, "w") as f:
        f.write("{}")
    f.close()
    
# Adds new data as entry in the JSON logfile
#### Modifier l'extension en log.txt quand j'aurai fini
def add_log_entry(new_entry : dict, log_name :str):
    log_path = os.path.join(os.getcwd(), "logs")
    logfile_path = os.path.join(log_path, log_name)
    json_file = open(logfile_path, "r")
    log = json.load(json_file)
    json_file.close()
    log.update({int(datetime.now().timestamp()):new_entry})
    file = open(logfile_path,"w")
    json.dump(log, file, indent=6)
    file.close()

def add_log_error (new_entry : dict, error_type : str):
    log_error_name = os.path.join(os.getcwd(), "log_errors.json")
    error_file = open(log_error_name, "r")
    log = json.load(error_file)
    error_file.close()
    log[error_type].update({int(datetime.now().timestamp()):new_entry})
    error_file = open(log_error_name,"w")
    json.dump(log, error_file, indent=6)
    error_file.close()