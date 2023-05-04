from fastapi import FastAPI
from datetime import datetime
from db import Barrier, Bell, Light, db

app = FastAPI()

#########################################################
## POST SECTION
# Added events are listed by their timestamp, converted in specified format (%Y-%m-%d %H:%M:%S)

@app.post("/barrier/{bar_id}")
def add_barrier_event (bar_id : int, event : Barrier):
   db["barriers"][f"barrier {bar_id}"][datetime.fromtimestamp(event.start_time).strftime('%Y-%m-%d %H:%M:%S')] = event
   return db["barriers"][f"barrier {bar_id}"]

@app.post("/bell/{bell_id}")
def add_bell_event (bell_id : int, event : Bell):
   db["bells"][f"bell {bell_id}"][datetime.fromtimestamp(event.start_time).strftime('%Y-%m-%d %H:%M:%S')] = event
   return db["bells"][f"bell {bell_id}"]
      
@app.post("/light/{light_id}")
def add_light_event (light_id : int, event : Light):
   db["lights"][f"light {light_id}"][datetime.fromtimestamp(event.start_time).strftime('%Y-%m-%d %H:%M:%S')] = event
   return db["lights"][f"light {light_id}"]
   
#########################################################
## GET SECTION

@app.get("/")
def read_root():
    return {"Hello": "World"}

#Get barrier with id
@app.get("/barriers/{item_id}")
def read_barrier_item(item_id: int):
   return db["barriers"][f"barrier {item_id}"]

#Get bell with id
@app.get("/bells/{item_id}")
def read_bell_item(item_id: int):
   return db["bells"][f"bell {item_id}"]

#Get light with id
@app.get("/lights/{item_id}")
def read_light_item(item_id: int):
   return db["lights"][f"light {item_id}"]


###########################################################
# If we need to access all the data from one source at once
# WIP

# #Get barrier without id
@app.get("/barriers")
def read_barrier():
   return db["barriers"]

#Get bell without id
@app.get("/bells")
def read_bell():
   return db["bells"]

#Get light without id
@app.get("/lights")
def read_light():
   return db["lights"]

###########################################################