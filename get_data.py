import requests
import os

# Functions to get informations from Uvicorn server

##################################################################
# TO BE IMPLEMENTED :
# CHANGE ADDRESS TO Point toward the server used and Elastic

#### A MODIFIER SELON L'ADRESSE UTILISÉE
url = "http://127.0.0.1:8000/" 

# Oxygen Platform end point on which data will be posted
# url= "https://pn89aulnoy.eairlink.com:27023"
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