from db import instanciate_captors
from get_data import *
from services import start_service, update_db ,get_uc_tocheck, uc_proc\
    # ,msg_data, print_db, print_new_data, print_get_data
import schedule, time

# Instanciate the recepting Database

captors= instanciate_captors()

# schedule.every(13).seconds.do(msg_data)
# time.sleep(1)

schedule.every(13).seconds.do(start_service)
time.sleep(1)

# schedule.every(13).seconds.do(print_get_data)
# time.sleep(1)
# schedule.every(13).seconds.do(print_new_data)
# time.sleep(1)

schedule.every(13).seconds.do(update_db, captors= captors)
time.sleep(1)

schedule.every(13).seconds.do(get_uc_tocheck)
schedule.every(13).seconds.do(uc_proc)

# schedule.every(13).seconds.do(print_db, captors= captors)
# time.sleep(1)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    

