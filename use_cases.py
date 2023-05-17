from db import associated_barriers
from script import sensors

####TO DO : IMPLEMENT THE LOG_ERROR ADRESSING TO ELASTIC SEARCH

## IMPLEMENT USE CASES 

# 1- Barrier not lowering 8 seconds after the lights are ON
def barrier_not_down(light_id : str):
    bar_id = associated_barriers.get(light_id)
    bar = sensors[bar_id]["cur"]   
    light = sensors[bar_id]["associated_light"][light_id]
    if bar.start_time == 0:
        print(f"ENVOYER UN MSG A ELK : Pas de données reçues pour la barrière {bar_id}")
    else :
        if bar.start_time - light.start_time > 8 :
            print("ENVOYER UN AUTRE MSG D'ERREUR A ELK : la barrière n'est pas abaissée à temps")

# 2- Barrier movement longer than 12 seconds
def barrier_islong(bar_id : str):
    bar = sensors[bar_id]["cur"]
    if bar.end_time - bar.start_time > 12 :
        print(f"ENCORE UN MSG D'ERREUR : LA BARRIERE {bar_id} EST TRES LONGUE")
    else :
        print ("TOU VA B1 !")

# 3- Abnormal position of the barrier after 20 seconds (non vertical or non horizontal)
def barrier_isregular(bar_id):
    bar_cur=  sensors[bar_id]["cur"]
    bar_pre=  sensors[bar_id]["pre"]
    if bar_cur.status == "irregular":
        if bar_cur.start_time - bar_pre.end_time > 20 :
            print(f"La barrière {bar_id} est dans un état CATATASTROPHIQUE MDR")
