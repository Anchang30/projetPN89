### Fichier test dans lequel j'ai repris la méthodologie utilisée pendant mon bootcamp
### Histoire de me refaire un peu la main

from fastapi import FastAPI
from data import PN
import os
import json

app = FastAPI()

barrier_list, barrier_path = PN().get_barrier_data()
bell_list, bell_path = PN().get_bell_data()
light_list, light_path = PN().get_light_data()

@app.get("/")
def read_root():
    return {"Hello": "World"}

#Get barrier without id
@app.get("/barriers")
def read_barrier():
    return {f"barrier n°{k}":json.load(open(os.path.join(barrier_path, v))) for k,v in (dict(enumerate(barrier_list,1))).items()}

#Get barrier with id
@app.get("/barriers/{item_id}")
def read_barrier_item(item_id: int):
    barrier_file_size = len(barrier_list)
    if item_id > barrier_file_size :
        return {f"We have no barrier n°{item_id}in  our data source":[]}
    else :
        barrier_file = f"{barrier_path}/barrier{item_id}.json"
        return {f"barrier n°{item_id}": json.load(open(barrier_file))}


#Get bell without id
@app.get("/bells")
def read_bell():
    return {f"bell n°{k}":json.load(open(os.path.join(bell_path, v))) for k,v in (dict(enumerate(bell_list,1))).items()}

#Get bell with id
@app.get("/bells/{item_id}")
def read_bell_item(item_id: int):
    bell_file_size = len(bell_list)
    if item_id > bell_file_size :
        return {f"We have no bell n°{item_id} in our data source":[]}
    else :
        bell_file = f"{bell_path}/bell{item_id}.json"
        return {f"bell n°{item_id}": json.load(open(bell_file))}


#Get light without id
@app.get("/lights")
def read_light():
    return {f"light n°{k}":json.load(open(os.path.join(light_path, v))) for k,v in (dict(enumerate(light_list,1))).items()}

#Get light with id
@app.get("/lights/{item_id}")
def read_light_item(item_id: int):
    light_file_size = len(light_list)
    if item_id > light_file_size :
        return {f"We have no light n°{item_id} in our data source":[]}
    else :
        light_file = f"{light_path}/light{item_id}.json"
        return {f"light n°{item_id}": json.load(open(light_file))}