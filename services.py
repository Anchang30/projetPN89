from get_data import add_log_entry, check_serv_status, get_data, get_serv_size, logfile_name
from use_cases import barrier_islong, barrier_isregular, barrier_not_down
import os

db_size = 0
new_data = []
uc_to_check = []
log_name = logfile_name()

# CHECKS IF NEW DATA AVAILABLE, STORE THEM IN NEW_DATA AND SAVE LOG_ENTRY
def start_service():   
    print('Searching for new data to collect')
    global db_size
    global new_data
    global log_name
    new_data = []
    print(f"{get_serv_size() - db_size} new data available")
    if check_serv_status(db_size) :
        add_log_entry(get_data()[db_size:], log_name) 
        new_data = get_data()[db_size:]
    db_size = get_serv_size()

# UPDATES BARRIER AND STATUS, BELL AND LIGHT ACCORDING TO NEW_DATA
def update_db(sensors):
    global new_data
    if new_data:
        print('Updating sensors with new data')
        for i in new_data[0]:
            id = i['GENERIC_DATA'][0]['device_name'] 
            if id.startswith("bar"):
                barrier_pre = sensors[id].get("prev")
                barrier_cur = sensors[id].get("cur")
                barrier_pre.update_barrier(barrier_cur.__dict__).update_barrier_status()
                barrier_cur.update_barrier(i['GENERIC_DATA'][0]).update_barrier_status()
            if id.startswith("bel"):
                for barrier in sensors :
                    try :                               #Update only the current bell with id
                        sensors[barrier]["associated_bell"].get(id).update_bell(i['GENERIC_DATA'][0])
                    except :                            #Don't update the other bells
                        sensors[barrier]["associated_bell"].get(id) == None
            if id.startswith("lig"):
                for barrier in sensors:
                    try :                               #Update current light with id
                        sensors[barrier]["associated_light"].get(id).update_light(i['GENERIC_DATA'][0])
                    except :                            #Don't update other lights
                        sensors[barrier]["associated_light"].get(id) == None
                       
# CREATES A LIST OF BARRIERS AND LIGHTS FOR USE CASES TO PROCESS
def get_uc_tocheck():
    global new_data
    global uc_to_check
    uc_to_check= []
    if new_data:
        print('Creating list of use cases')
        for i in new_data[0]:
            id = i['GENERIC_DATA'][0]['device_name'] 
            if id.startswith("bar") and id not in uc_to_check:
                uc_to_check.append(id)

# PROCESSES DATA ACCORDING TO USER CASES
def uc_proc(sensors : dict):
    global uc_to_check
    if uc_to_check :
        print('Processing use cases')
        for id in uc_to_check :
            barrier_not_down(id, sensors)
            barrier_islong(id, sensors)
            barrier_isregular(id, sensors)
    uc_to_check = []
