from db import Barrier, Bell, Light, instanciate_captors
from get_data import *
from services import start_service, update_db
import schedule, time

# Instanciate the recevor Database
db_size = 0
db_get_list = []
captors = instanciate_captors()
db_cur = []
# Regular task checking for new data
serv_size = get_serv_size()

schedule.every(10).seconds.do(start_service, db_get_list= db_get_list, db_get_cur= db_cur)

schedule.every(10).seconds.do(update_db, captors = captors, db_cur= db_cur)

####################################################################

# # IMPLEMENT USE CASES 

# # 1- not_down()
# # barrière non abaissée après 8 secondes d'allumage des FEUX

# # 2- islong()
# # Mouvement d'une barrière de plus de 12s

# # 3- isregular()s
# # Positionnement anormal d'une barrière plus de 20 s

###########################################

while True:
    schedule.run_pending()
    time.sleep(1)
    
    

