from es_management import add_log_error
from elasticsearch import Elasticsearch
from db import associated_barriers, Barrier, Light
import time

## IMPLEMENT USE CASES 

# 1- Barrier not lowering 8 seconds after the lights are ON
## Saves multiple log_error because there are 2 lights per barrier
def barrier_not_down(es: Elasticsearch, light : Light, sensors : dict):
    bar_id = associated_barriers[light.device_name]
    bar = sensors[bar_id]["lower"]
    if bar.start_time == 0:
        add_log_error(es, bar, "no data")
        print("Log error 'no data' sent to ElasticSearch")
    else :
        if bar.start_time - light.start_time > 8 :
            add_log_error(es, bar, "not down")
            print("Log error 'not down' sent to ElasticSearch")

# 2- Barrier movement longer than 12 seconds
def barrier_islong(es :Elasticsearch, barrier : Barrier):
    if barrier.end_time - barrier.start_time > 12 :
        add_log_error(es, barrier, "is long") 
        print("Log error 'is long' sent to ElasticSearch")

# 3- Abnormal position of the barrier after 20 seconds (non vertical or non horizontal)
def barrier_isregular(es: Elasticsearch, barrier : Barrier):
    if barrier.status == "lower":
        if barrier.end_angle != 0 and barrier.end_time - int(time.time()) > 20 :
            add_log_error(es, barrier, "irregular")
            print("Log error 'irregular' sent to ElasticSearch")
    elif barrier.status == "rise":  
        if barrier.end_angle != 90 and barrier.end_time - int(time.time()) > 20 :
            add_log_error(es, barrier, "irregular")
            print("Log error 'irregular' sent to ElasticSearch")
