from get_data import add_log_entry, check_serv_status, get_data, get_serv_size

def msg_data():
    print("Fetching new data")
def print_get_data():
    print(get_data())
    
db_size=0
new_data= []

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

def print_new_data():
    global new_data
    print(new_data)
    
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
def print_db(captors):
    print(captors["bar-c100x-abcd1234"])