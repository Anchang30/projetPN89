from db import associated_barriers
from get_data import add_log_error

####TO DO : IMPLEMENT THE LOG_ERROR ADRESSING TO ELASTIC SEARCH
#### FOR NOW, IT IS POITING TO A LOCAL JSON LOG_ERROR

## IMPLEMENT USE CASES 

# 1- Barrier not lowering 8 seconds after the lights are ON
## ENREGISTRE PLUSIEURS LOG_ERREUR CAR JE PARSE TOUTES LES LUMIRES ASSOCIÉES A UNE BARRIERE
## DONC SI J4AI DEUX LUMIERES, J'OBTIENS DEUX LOGS D'ERREUR (UN POUR CHACUNE)
def barrier_not_down(bar_id : str, sensors : dict):
    bar = sensors[bar_id]["prev"]   
    lights = sensors[bar_id]["associated_light"]
    if bar.start_time == 0:
        print(f"ENVOYER UN MSG A ELK : Pas de données reçues pour la barrière {bar_id}")
    else :
        for light in lights.values() :
            if bar.start_time - light.start_time > 8 :
                print("ENVOYER UN AUTRE MSG D'ERREUR A ELK : la barrière n'est pas abaissée à temps")
                add_log_error(bar.__dict__, "barrier_not_down")    

# 2- Barrier movement longer than 12 seconds
def barrier_islong(bar_id : str, sensors : dict):
    bar = sensors[bar_id]["cur"]
    if bar.end_time - bar.start_time > 12 :
        print(f"ENCORE UN MSG D'ERREUR : LA BARRIERE {bar_id} EST TRES LONGUE")
        add_log_error(bar.__dict__, "barrier_is_long")

# 3- Abnormal position of the barrier after 20 seconds (non vertical or non horizontal)
def barrier_isregular(bar_id : int , sensors : dict):
    bar_cur = sensors[bar_id]["cur"]
    bar_pre = sensors[bar_id]["prev"]
    if bar_cur.status == "irregular":
        if bar_cur.start_time - bar_pre.end_time > 20 :
            print(f"La barrière {bar_id} est dans un état CATATASTROPHIQUE MDR")
            add_log_error(bar_cur.__dict__, "barrier_is_irregular")
