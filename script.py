from db import instanciate_sensors
from get_data import *
from services import start_service, update_db ,get_uc_tocheck, uc_proc
import schedule, time


##################################################################
# TBI : Change the time window for checking updates in new data
##################################################################


#Logging creates a log_file with a new name for each session in the services module

# Instanciates the receiving Database
sensors= instanciate_sensors()
# Checks if new data available
schedule.every(13).seconds.do(start_service)
time.sleep(1)
# If new data, updates database 
schedule.every(13).seconds.do(update_db, sensors = sensors)
time.sleep(1)
# Creates a list with new values on which user cases apply
schedule.every(13).seconds.do(get_uc_tocheck)
# Processes use cases and clean the previous list for a new iteration
schedule.every(13).seconds.do(uc_proc, sensors = sensors)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    

