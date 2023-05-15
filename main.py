from fastapi import FastAPI
from typing import Any, Dict, AnyStr, List, Union

app = FastAPI()
db_post = []

JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]

#########################################################
## POST SECTION

@app.post("/")
def post_root(arbitrary_json: JSONStructure = None):
   db_post.append(arbitrary_json)
   return db_post
   
#########################################################
## GET SECTION

@app.get("/")
def get_root():
   return db_post

#########################################################

