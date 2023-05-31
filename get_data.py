import json
import requests
from datetime import datetime
import os

##################################################################
# TO BE IMPLEMENTED :
# CHANGE ADDRESS TO Point toward the server used and Elastic
# Modify the log_error function to store these info in the Elastic 

# Functions to get informations from Uvicorn server
#### A MODIFIER SELON L'ADRESSE UTILISÉE
url = "http://127.0.0.1:8000/" 
##################################################################


# Gets all data from server
def get_data():
    return requests.get(url).json()

# Gets server size to remember where to continue parsing
def get_serv_size():
    return len(get_data())

# Gets server status if new data available
def check_serv_status(db_size : int):
    serv_size = get_serv_size()
    if serv_size > db_size:
        return f"{serv_size - db_size} new data available"
    
# CREATES LOG FOLDER IF IT DOESNT EXIST AND RETURN THE NB OF LOG FILES IN IT 
# TO GENERATE THE NAME OF THE CURRENT LOG FILE
def logfile_name():
    path_ = os.getcwd()
    log_path = os.path.join(os.getcwd(), "logs")
    if "logs" not in os.listdir(path_):
        os.mkdir(log_path)
    len_json = len([doc for doc in os.listdir(log_path) if doc.startswith("log") and doc.endswith(".txt")])
    if len_json == 0:
        return "log.txt"
    else :
        return f"log{len_json}.txt"

# IF A USE CASE IS VALIDATED (THERE'S AN ERROR), THIS FUNCTION SENDS AN ERROR MESSAGE TO
# A LOG_ERRORS FILE (JSON FOR NOW).
# TBI : LINK THIS TO ELASTIC SEARCH
def add_log_error (new_entry : dict, error_type : str):
    log_error_name = os.path.join(os.getcwd(), "log_errors.json")
    error_file = open(log_error_name, "r")
    log = json.load(error_file)
    error_file.close()
    log[error_type].update({int(datetime.now().timestamp()):new_entry})
    error_file = open(log_error_name,"w")
    json.dump(log, error_file, indent=6)
    error_file.close()