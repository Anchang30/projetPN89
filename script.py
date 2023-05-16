from db import instanciate_captors
from get_data import *
from services import start_service, update_db, msg_data, print_db, print_new_data, print_get_data
import schedule, time

# Instanciate the recepting Database

captors= instanciate_captors()

schedule.every(13).seconds.do(msg_data)
time.sleep(1)
schedule.every(13).seconds.do(start_service)
time.sleep(1)
schedule.every(13).seconds.do(print_get_data)
time.sleep(1)
schedule.every(13).seconds.do(print_new_data)
time.sleep(1)
schedule.every(13).seconds.do(update_db, captors= captors)
time.sleep(1)
schedule.every(13).seconds.do(print_db, captors= captors)
time.sleep(1)

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
    
    

