from db import instanciate_sensors
from get_data import *
from services import start_service, update_db, uc_proc
import schedule, time
from es_management import instanciate_es, create_es_index


##################################################################
# TBI : Change the time window for checking updates in new data
##################################################################

# Instanciates the receiving Database
sensors= instanciate_sensors()
# Instanciates the ElasticSearch 
es = instanciate_es()
# Creates the index for PN89 if not existant
create_es_index(es)
# Checks if new data available
schedule.every(13).seconds.do(start_service)
time.sleep(1)
# If new data, updates database and create a list of UC to check
schedule.every(13).seconds.do(update_db, sensors = sensors)
time.sleep(1)
# Processes use cases and clean the previous list for a new iteration
schedule.every(13).seconds.do(uc_proc, es=es, sensors = sensors)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    

