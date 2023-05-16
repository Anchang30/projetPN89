from get_data import add_log_entry, check_serv_status, get_data, get_serv_size

db_size = 0

def start_service(db_get_list, db_get_cur):   
    global db_size
    if check_serv_status(db_size) :
        print('je récupère une db de ', db_size)
        db_get_cur = []
        add_log_entry(get_data()[db_size:])
        db_get_list.append(get_data())
        db_get_cur.append(get_data()[db_size:])
    db_size = get_serv_size()


def update_db(captors, db_cur):
    if db_cur:
        for i in db_cur:
            if i['GENERIC_DATA'][0]['device_name'].startswith("bar"):
                barrier_id = i['GENERIC_DATA'][0]['device_name']
                barrier_pre = captors[barrier_id].get("prev")
                barrier_cur = captors[barrier_id].get("cur")
                barrier_pre.update_barrier(barrier_cur.__dict__)
                barrier_cur.update_barrier(i['GENERIC_DATA'][0])
                
            if i['GENERIC_DATA'][0]['device_name'].startswith("bel"):
                bell_id = i['GENERIC_DATA'][0]['device_name']
                for barrier in captors :
                    bell= captors[barrier]["associated_bell"].get(bell_id)
                    try :
                        bell= captors[barrier]["associated_bell"].get(bell_id)
                        bell.update_bell(i['GENERIC_DATA'][0])
                    except :
                        captors[barrier]["associated_bell"].get(bell_id) == None
                    
            if i['GENERIC_DATA'][0]['device_name'].startswith("lig"):
                light_id = i['GENERIC_DATA'][0]['device_name']
                for barrier in captors:
                    try :
                        light = captors[barrier]["associated_light"].get(light_id)
                        light.update_light(i['GENERIC_DATA'][0])
                    except :
                        captors[barrier]["associated_light"].get(light_id) == None
                    