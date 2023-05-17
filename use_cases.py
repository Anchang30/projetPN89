from db import associated_barriers
from script import captors

# IMPLEMENT USE CASES 
# 1- check_barrier_not_down()
# barrière non abaissée après 8 secondes d'allumage des FEUX

"""COMME on reçoit les feux en dernier,
des réception de data "light" : if i['GENERIC_DATA'][0]['device_name'].startswith("lig")
    on update les feux
    on récupère la barrière associée
    on vérifie si start time barrière != 0
    on calcule bar.start_time - light.start_time > 8 :
        renvoie un msg d'erreur sur Elastic"""

####IMPLEMENT THE LOG_ERROR ADRESSING TO ELASTIC SEARCH
def barrier_not_down(light_id : str):
    bar_id = associated_barriers.get(light_id)
    bar = captors[bar_id]["cur"]   
    light = captors[bar_id]["associated_light"][light_id]
    if bar.start_time == 0:
        print(f"ENVOYER UN MSG A ELK : Pas de données reçues pour la barrière {bar_id}")
    else :
        if bar.start_time - light.start_time > 8 :
            print("ENVOYER UN AUTRE MSG D'ERREUR A ELK : la barrière n'est pas abaissée à temps")

# 2- check_barrier_islong()
# Mouvement d'une barrière de plus de 12s

def barrier_islong(bar_id : str):
    bar = captors[bar_id]["cur"]
    if bar.end_time - bar.start_time > 12 :
        print(f"ENCORE UN MSG D'ERREUR : LA BARRIERE {bar_id} EST TRES LONGUE")
    else :
        print ("TOU VA B1 !")


# 3- check_barrier_isregular()
# Positionnement anormal d'une barrière plus de 20 s (non vertical ou non horizontal)

def barrier_isregular(bar_id):
    bar_cur=  captors[bar_id]["cur"]
    bar_pre=  captors[bar_id]["pre"]
    if bar_cur.status == "irregular":
        if bar_cur.start_time - bar_pre.end_time > 20 :
            print(f"La barrière {bar_id} est dans un état CATATASTROPHIQUE MDR")


