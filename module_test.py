# from db import Barrier, Bell, Light, instanciate_captors
# from get_data import *
# from services import start_service, update_db
# from script import db_size, db_get_list, db_get_cur, serv_size, captors
from schedule import every, repeat, run_pending
import time
from datetime import datetime

# ## FICHIER TEST TANT QUE JE N4AI PAS IMPLEMENT2 LE SCHEDULE, POUR NE PAS RAZ LES VARIABLES
# print(db_size)
# db_size, db_get_list, db_get_cur, serv_size = start_service(db_size, db_get_list, db_get_cur, serv_size)
# print(db_size)
# print(db_get_cur)
# # Mise à jour des variables capteurs reçues par la requête get
# update_db(captors, db_get_cur)
# print(captors["captor_list"]['barriers'])



# def greet(name):
#     print('Hello', name)

# def time_now():
#     print(datetime.now().strftime("%a %d %H:%M:%S"))
    
# schedule.every(5).seconds.do(greet, name='Alice')
# schedule.every(7).seconds.do(greet, name='Bob')
# schedule.every().seconds.do(time_now)
# from schedule import every, repeat

# @repeat(every(3).seconds, "World")
# @repeat(every().minutes, "Mars")
# def hello(planet):
#     print("Hello", planet)

x=5
@repeat(every(3).seconds)
def yee():
    global x
    x *= 2
    print(x)    


while True:
    run_pending()
    time.sleep(1)