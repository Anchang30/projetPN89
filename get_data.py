import json
from main import read_barrier, read_bell, read_light
import requests

# Fonction pour récupérer automatiquement les données sur le serveur Uvicorn


url = "http://127.0.0.1:8000/"

def get_barriers():
    query = url + "barriers"
    response_bar = requests.get(query).json()
    save_file = open("data/barrier_files/all_barriers_json", "w")
    json.dump(response_bar, save_file, indent= 6)
    print("barriers JSON file saved !")
    save_file.close()

def get_bells():
    query = url + "bells"
    response_bel = requests.get(query).json()
    save_file = open("data/bell_files/all_bells_json", "w")
    json.dump(response_bel, save_file, indent= 6)
    print("bells JSON file saved !")
    save_file.close()

def get_lights():
    query = url + "lights"
    response_lg = requests.get(query).json()
    save_file = open("data/light_files/all_lights_json", "w")
    json.dump(response_lg, save_file, indent= 6)
    print("lights JSON file saved !")
    save_file.close()

def read_json():
    print("LOADING SAVED JSON")
    f = open("data/barrier_files/whole_barrier_json")
    my_json_file = json.load(f)
    print(my_json_file)
        

