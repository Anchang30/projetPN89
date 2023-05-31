from get_data import add_log_error
# from es_management import es

## IMPLEMENT USE CASES 

# 1- Barrier not lowering 8 seconds after the lights are ON
## Saves multiple log_error because there are 2 lights per barrier
def barrier_not_down(bar_id : str, sensors : dict):
    bar = sensors[bar_id]["prev"]   
    lights = sensors[bar_id]["associated_light"]
    if bar.start_time == 0:
        add_log_error(bar, "no data")
    else :
        for light in lights.values() :
            if bar.start_time - light.start_time > 8 :
                add_log_error(bar, "not down")

# 2- Barrier movement longer than 12 seconds
def barrier_islong(bar_id : str, sensors : dict):
    bar = sensors[bar_id]["cur"]
    if bar.end_time - bar.start_time > 12 :
        add_log_error(bar, "is long") 

# 3- Abnormal position of the barrier after 20 seconds (non vertical or non horizontal)
def barrier_isregular(bar_id : int , sensors : dict):
    bar_cur = sensors[bar_id]["cur"]
    bar_pre = sensors[bar_id]["prev"]
    if bar_cur.status == "irregular":
        if bar_cur.start_time - bar_pre.end_time > 20 :
            add_log_error(bar_cur, "irregular")
