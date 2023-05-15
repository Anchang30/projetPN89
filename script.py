from db import Barrier, Bell, Light, instanciate_captors
from get_data import *
from services import start_service, update_db
import schedule, time

# Instanciate the recevor Database
db_size = 0
db_get_list = []
captors = instanciate_captors()
db_get_cur = []
# Regular task checking for new data
serv_size = get_serv_size()

############
#TEST A VIRER
# def print_db():
#     print("tDb taille est de", db_size)
    
############
#TEST A VIRER
# @schedule.repeat(schedule.every(10).seconds)
# def serv_count():
#     global serv_size
#     serv_size = get_serv_size()
#     print("Serveur est de ", serv_size) 
# time.sleep(1)

schedule.every(10).seconds.do(start_service, db_get_list= db_get_list, db_get_cur= db_get_cur)
############
#TEST A VIRER
# schedule.every(10).seconds.do(print_db)
schedule.every(10).seconds.do(update_db, captors = captors, db_get_cur= db_get_cur)
############
#TEST A VIRER
# time.sleep(1) 
# @schedule.repeat(schedule.every(10).seconds)
# def update_db_size():
#     global db_size, serv_size
#     db_size= get_serv_size()
#     print("La taille réelle de la db es", db_size)


while True:
    schedule.run_pending()
    # db_size = start_service(db_size, db_get_list, db_get_cur, serv_size)
    time.sleep(1)
####################################################################
# on reboucle ici pour ajouter les nouvelles données
# start_service(db_size, db_get_list, db_get_cur, serv_size)
# print(db_size, serv_size)
# print(db_get_cur)
# # IMPLEMENT USE CASES 

# # 1- not_down()
# # barrière non abaissée après 8 secondes d'allumage des FEUX

# # 2- islong()
# # Mouvement d'une barrière de plus de 12s

# # 3- isregular()s
# # Positionnement anormal d'une barrière plus de 20 s


# # Mise à jour des variables capteurs reçues par la requête get
# update_db(captors, db_get_cur)
            
# print(captors["captor_list"]['barriers'])
###########################################""
# Et on reboucle plus haut