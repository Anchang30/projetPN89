from get_data import add_log_entry, check_serv_status, get_data, get_serv_size
from db import Barrier, Bell, Light

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


def update_db(captors, db_get_cur):
    if db_get_cur:
        for i in db_get_cur[0]:
            if i['GENERIC_DATA'][0]['device_name'].startswith("bar"):
                barrier_id = i['GENERIC_DATA'][0]['device_name']
                barrier_pre = captors['captor_list']['barriers'].get(barrier_id+"_pre")
                barrier_cur = captors['captor_list']['barriers'].get(barrier_id+"_cur")
                barrier_pre.update_barrier(barrier_cur.__dict__)
                barrier_cur.update_barrier(i['GENERIC_DATA'][0])
            if i['GENERIC_DATA'][0]['device_name'].startswith("bel"):
                bell_id = i['GENERIC_DATA'][0]['device_name']
                bell_pre = captors['captor_list']['bells'].get(bell_id+"_pre")
                bell_cur = captors['captor_list']['bells'].get(bell_id+"_cur")
                bell_pre.update_bell(bell_cur.__dict__)
                bell_cur.update_bell(i['GENERIC_DATA'][0])
            if i['GENERIC_DATA'][0]['device_name'].startswith("lig"):
                light_id = i['GENERIC_DATA'][0]['device_name']
                light_pre = captors['captor_list']['lights'].get(light_id+"_pre")
                light_cur = captors['captor_list']['lights'].get(light_id+"_cur")
                light_pre.update_light(light_cur.__dict__)
                light_cur.update_light(i['GENERIC_DATA'][0])