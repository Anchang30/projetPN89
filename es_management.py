from elasticsearch import Elasticsearch
from db import Barrier

# Instanciates the ElasticSearch (ES)
# ADRESSE A CHANGER POUR POINTER VERS LE ELASTIC ??

def instanciate_es ():
    es = Elasticsearch("http://localhost:9200")
    return es
    
def create_es_index(es: Elasticsearch):
    global index_name
    index_name = "pn89_log_error"
    # Get a list of indices
    index_list = es.cat.indices(h='index', s='index').split()

    # Creates the mapping for the ES db
    mapping_barrier = {
        "properties" : {
            "id": {"type" : "integer"},
            "device_name" : {"type": "text"},
            "start_time" : {"type" : "date", "format" : "epoch_second"},
            "start_angle": {"type" : "integer"},
            "end_time": {"type" : "date", "format" : "epoch_second"},
            "end_angle": {"type" : "integer"},
            "status": {"type" : "text"},
            "error_type" : {"type" : "text"}
    }}


    # Creates the index for log_error if it doesn't exist yet
    if index_name not in index_list :
        es.indices.create(index=index_name, mappings=mapping_barrier)
        

# Function to add errors as log in ES with class instanciation and error_type
def add_log_error(es: Elasticsearch, bar: Barrier, error_type: str):
    doc = bar.__dict__.copy()
    doc["error_type"] = error_type 
    es.index(index=index_name, document=doc)
