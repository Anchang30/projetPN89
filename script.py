from db import instanciate_sensors
from get_data import *
from services import start_service, update_db ,get_uc_tocheck, uc_proc, logfile_name, create_logfile
import schedule, time

# CHECKS IF LOGS FOLDER
log_name = create_logfile()
#CREATES A NEW LOGFILE IN IT
create_logfile(log_name)
# Instanciates the recepting Database
sensors= instanciate_sensors()
# Checks if new data available
schedule.every(13).seconds.do(start_service(log_name= log_name))
time.sleep(1)
# Updates database if new data
schedule.every(13).seconds.do(update_db, sensors= sensors)
time.sleep(1)
# Creates a list with new values on which user cases apply
schedule.every(13).seconds.do(get_uc_tocheck)
# Processes with use cases and clean the previous list for a new iteration
schedule.every(13).seconds.do(uc_proc)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    

