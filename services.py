from get_data import add_log_entry, check_serv_status, get_data, get_serv_size
from use_cases import barrier_islong, barrier_isregular, barrier_not_down
import os

db_size=0
new_data= []
uc_to_check= []

# CREATES LOG FOLDER IF IT DOESNT EXIST AND RETURN THE NB OF LOG FILES IN IT
def logfile_name():
    path_ = os.getcwd()
    log_path= os.path.join(os.getcwd(), "logs")
    if "logs" not in os.listdir(path_):
        os.mkdir(log_path)
    len_json = len([doc for doc in os.listdir(log_path) if doc.startswith("log") and doc.endswith(".json")])
    if len_json == 0:
        return "log.json"
    else :
        return f"log{len_json}.json"

# CREATES A NEW LOGFILE FOR EACH NEW SESSION    
def create_logfile(log_name : str):
    log_path = os.path.join(os.getcwd(), "logs")
    logfile_path = os.path.join(log_path, log_name)
    with open(logfile_path, "w") as f:
        f.write("{}")
    f.close()

# CHECKS IF NEW DATA AVAILABLE, STORE THEM IN NEW_DATA AND SAVE LOG_ENTRY
def start_service():   
    global db_size
    global new_data
    new_data= []
    if check_serv_status(db_size) :
        print(f"{get_serv_size() - db_size} new data available")
        add_log_entry(get_data()[db_size:]) 
        new_data = get_data()[db_size:]
    db_size = get_serv_size()

# UPDATES BARRIER AND STATUS, BELL AND LIGHT ACCORDING TO NEW_DATA
def update_db(sensors):
    global new_data
    if new_data:
        for i in new_data[0]:
            id =i['GENERIC_DATA'][0]['device_name'] 
            if id.startswith("bar"):
                barrier_pre = sensors[id].get("prev")
                barrier_cur = sensors[id].get("cur")
                barrier_pre.update_barrier(barrier_cur.__dict__)
                barrier_cur.update_barrier(i['GENERIC_DATA'][0])
                barrier_pre.update_barrier_status()
                barrier_cur.update_barrier_status()
            if id.startswith("bel"):
                for barrier in sensors :
                    bell= sensors[barrier]["associated_bell"].get(id)
                    try :
                        bell= sensors[barrier]["associated_bell"].get(id)
                        bell.update_bell(i['GENERIC_DATA'][0])
                    except :
                        sensors[barrier]["associated_bell"].get(id) == None
            if id.startswith("lig"):
                for barrier in sensors:
                    try :
                        light = sensors[barrier]["associated_light"].get(id)
                        light.update_light(i['GENERIC_DATA'][0])
                    except :
                        sensors[barrier]["associated_light"].get(id) == None
                       
# CREATES A LIST OF BARRIERS AND LIGHTS FOR USE CASES TO PROCESS
def get_uc_tocheck():
    global new_data
    global uc_to_check
    uc_to_tocheck= []
    if new_data:
        for i in new_data[0]:
            id= i['GENERIC_DATA'][0]['device_name'] 
            if id.startswith("lig") or id.startswith("bar"):
                uc_to_tocheck.append(id)

# PROCESSES DATA ACCORDING TO USER CASES
def uc_proc():
    for id in uc_to_check :
        if id.startswith("lig"):
            print('salut')
            barrier_not_down(id)
        else:
            print('coucou')
            barrier_islong(id)
            barrier_isregular(id)
    uc_to_check = []
