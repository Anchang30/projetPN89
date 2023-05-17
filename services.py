from get_data import add_log_entry, check_serv_status,\
    get_data, get_serv_size
from use_cases import barrier_islong, barrier_isregular, barrier_not_down


db_size=0
new_data= []
uc_to_check= []

# CHECK IF NEW DATA AVAILABLE, STORE THEM IN NEW_DATA AND SAVE LOG_ENTRY
def start_service():   
    global db_size
    global new_data
    new_data= []
    if check_serv_status(db_size) :
        print(f"{get_serv_size() - db_size} new data available")
        add_log_entry(get_data()[db_size:]) 
        # db_get_list.append(get_data())
        new_data = get_data()[db_size:]
    db_size = get_serv_size()

# UPDATE BARRIER AND STATUS, BELL AND LIGHT ACCORDING TO NEW_DATA
def update_db(captors):
    global new_data
    if new_data:
        for i in new_data[0]:
            id =i['GENERIC_DATA'][0]['device_name'] 
            
            if id.startswith("bar"):
                barrier_pre = captors[id].get("prev")
                barrier_cur = captors[id].get("cur")
                barrier_pre.update_barrier(barrier_cur.__dict__)
                barrier_cur.update_barrier(i['GENERIC_DATA'][0])
                barrier_pre.update_barrier_status()
                barrier_cur.update_barrier_status()
                
            if id.startswith("bel"):
                for barrier in captors :
                    bell= captors[barrier]["associated_bell"].get(id)
                    try :
                        bell= captors[barrier]["associated_bell"].get(id)
                        bell.update_bell(i['GENERIC_DATA'][0])
                    except :
                        captors[barrier]["associated_bell"].get(id) == None
                    
            if id.startswith("lig"):
                for barrier in captors:
                    try :
                        light = captors[barrier]["associated_light"].get(id)
                        light.update_light(i['GENERIC_DATA'][0])
                    except :
                        captors[barrier]["associated_light"].get(id) == None
                       
# CREATE A LIST OF BARRIERS AND LIGHTS FOR USE CASES TO PROCESS
def get_uc_tocheck():
    global new_data
    global uc_to_check
    uc_to_tocheck= []
    if new_data:
        for i in new_data[0]:
            id= i['GENERIC_DATA'][0]['device_name'] 
            if id.startswith("lig") or id.startswith("bar"):
                uc_to_tocheck.append(id)

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
    
#################################################################
# TO REMOVE AFTER DEV COMPLETION             
def msg_data():
    print("Checking if new data")
    
def print_get_data():
    print(get_data())
    
def print_new_data():
    global new_data
    print(new_data)                           
                        
def print_db(captors):
    print(captors["bar-c100x-abcd1234"])
    ##############################################################