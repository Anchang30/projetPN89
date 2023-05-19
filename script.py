from db import instanciate_sensors
from get_data import *
from services import start_service, update_db ,get_uc_tocheck, uc_proc
import schedule, time

# CHECKS IF LOGS FOLDER
create_logfile(logfile_name())
#CREATES A NEW LOGFILE IN IT
# Instanciates the recepting Database
sensors= instanciate_sensors()
# Checks if new data available
schedule.every(13).seconds.do(start_service)
time.sleep(1)
# Updates database if new data
schedule.every(13).seconds.do(update_db, sensors = sensors)
time.sleep(1)
# Creates a list with new values on which user cases apply
schedule.every(13).seconds.do(get_uc_tocheck)
# Processes with use cases and clean the previous list for a new iteration
schedule.every(13).seconds.do(uc_proc, sensors = sensors)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    

