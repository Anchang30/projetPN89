from get_data import  *
from use_cases import barrier_islong, barrier_isregular, barrier_not_down
import logging
from importlib import reload
import os
from elasticsearch import Elasticsearch
from db import Barrier

# Instanciates every variable used, as well as the logging object for log_storage
db_size = 0
new_data = []
uc_to_check = []
log_name = logfile_name()
log_path = os.path.join(os.getcwd(), "logs", log_name)
reload(logging)
logging.basicConfig(filename=log_path, encoding='utf-8', \
    level=logging.INFO ,format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S')

# Checks if new data available, store them in new_data and save log_entry
def start_service():   
    print('Searching for new data to collect')
    global db_size
    global new_data
    global log_name
    new_data = []
    print(f"{get_serv_size() - db_size} new data available")
    if check_serv_status(db_size) :
        logging.info(get_data()[db_size:])
        new_data = get_data()[db_size:]
    db_size = get_serv_size()

# Updates barrier and status, bell and light according to new_data
def update_db(sensors):
    global new_data
    global uc_to_check
    if new_data:
        print('Updating sensors with new data')
        for ele in new_data:
            for i in ele :
                # gets device name
                id = i['GENERIC_DATA'][0]['device_name'] 
                # gets data to update
                data_to_update = i['GENERIC_DATA'][0]
                if id.startswith("bar"):
                    # gets database sensor to update
                    barrier = sensors[id]
                    if data_to_update["start_angle"] > data_to_update["end_angle"] :
                        barrier["lower"].update_barrier(data_to_update).update_barrier_status()
                        uc_to_check.append(barrier["lower"])
                    else:
                        barrier["rise"].update_barrier(data_to_update).update_barrier_status()
                        uc_to_check.append(barrier["rise"])
                if id.startswith("bel"):
                    for barrier in sensors :
                        try :                               #Update only the current bell with id
                            sensors[barrier]["associated_bell"].get(id).update_bell(data_to_update)
                        except :                            #Don't update the other bells
                            sensors[barrier]["associated_bell"].get(id) == None
                if id.startswith("lig"):
                    for barrier in sensors:
                        try :                               #Update current light with id
                            sensors[barrier]["associated_light"].get(id).update_light(data_to_update)
                            uc_to_check.append(sensors[barrier]["associated_light"][id]) 
                        except :                            #Don't update other lights
                            sensors[barrier]["associated_light"].get(id) == None
 
# Processes data according to use cases
def uc_proc(es : Elasticsearch, sensors : dict):
    global uc_to_check
    if uc_to_check :
        print('Processing use cases')
        for ele in uc_to_check :
            if ele.device_name.startswith("lig"):
                barrier_not_down(es, ele, sensors)
            else: 
                barrier_islong(es, ele)
                barrier_isregular(es, ele)
    uc_to_check = []
