from random import uniform
import json

# CREATION DES DATASETS
train_list = ["881235","2256", "881766", "880447", "881235", "2389",\
    "882559", "881766", "880447", "1759", "97653", "2357", "883496", "875963",\
        "882559", "1356", "5562", "881236", "880465", "5573"]
timestamp_list = [1683012695, 1683015972, 1683016276, 1683017804, 1683022304, 1683026642, 1683027371, 1683027911,\
    1683029116, 1683030616, 1683032248, 1683033193, 1683036116, 1683036683, 1683039646, 1683041565, 1683043426,\
        1683045201, 1683047636,1683048370]
pn_list = [str(ele) for ele in [1,2,1,1,2,1,1,2,2,1,1,2,1,1,2,1,2,1,2,1]]
problem_list = [str(ele).replace("0","False").replace("1","True") for ele in [0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0]]

fused_data = list(zip(pn_list, train_list, timestamp_list, problem_list))

# CREATION DES DICTIONNAIRES
bar_dict= dict([(f"barrier {i}", {}) for i in range (1,5)])
bel_dict= dict([(f"bell {i}", {}) for i in range (1,5)])
lig_dict= dict([(f"light {i}", {}) for i in range (1,11)])

# CREATION DU JSON BARRIERS

for i in fused_data:
    if i[0] == "1":
        for j in range(1,3):
            if i[3] == "True":
                bar_dict[f"barrier {j}"][i[1]] = [{
                    "device_name": "stu-c100x-abcd1234",
                    "start_time": i[2]+8,
                    "start_angle": 90.0 + uniform(-5, 5),
                    "end_time": i[2]+12,
                    "end_angle": 0.0 + uniform(-5,5)
                    }]
                bar_dict[f"barrier {j}"][i[1]].append({
                    "device_name": "stu-c100x-abcd1234",
                    "start_time": i[2]+65,
                    "start_angle": 0.0,
                    "end_time": i[2] +77,
                    "end_angle": 90.0
                    })
            else :
                bar_dict[f"barrier {j}"][i[1]] = [{
                    "device_name": "stu-c100x-abcd1234",
                    "start_time": i[2]+8,
                    "start_angle": 90.0,
                    "end_time": i[2]+12,
                    "end_angle": 0.0
                    }]
                bar_dict[f"barrier {j}"][i[1]].append({
                    "device_name": "stu-c100x-abcd1234",
                    "start_time": i[2]+65,
                    "start_angle": 0.0,
                    "end_time": i[2] +77,
                    "end_angle": 90.0
                    })
    elif i[0] == "2" :
        for j in range(3,5):
            if i[3] == "True":
                bar_dict[f"barrier {j}"][i[1]] = [{
                    "device_name": "stu-c100x-abcd1234",
                    "start_time": i[2]+8,
                    "start_angle": 90.0 + uniform(-5, 5),
                    "end_time": i[2]+12,
                    "end_angle": 0.0 + uniform(-5,5)
                    }]
                bar_dict[f"barrier {j}"][i[1]].append({
                    "device_name": "stu-c100x-abcd1234",
                    "start_time": i[2]+65,
                    "start_angle": 0.0,
                    "end_time": i[2] +77,
                    "end_angle": 90.0
                    })
            bar_dict[f"barrier {j}"][i[1]] = [{
                    "device_name": "stu-c100x-abcd1234",
                    "start_time": i[2]+8,
                    "start_angle": 90.0,
                    "end_time": i[2]+12,
                    "end_angle": 0.0
                    }]
            bar_dict[f"barrier {j}"][i[1]].append({
                "device_name": "stu-c100x-abcd1234",
                "start_time": i[2]+65,
                "start_angle": 0.0,
                "end_time": i[2] +77,
                "end_angle": 90.0
                })

# CREATION DU JSON BELLS

for i in fused_data:
    if i[0] == "1":
        for j in range(1,3):
            bel_dict[f"bell {j}"][i[1]] = {
                "device_name": "stu-c100x-abcd1234",
                "start_time": i[2],
                "end_time": i[2]+8,
                }
    elif i[0] == "2":
        for j in range(3,5):
            bel_dict[f"bell {j}"][i[1]] = {
                "device_name": "stu-c100x-abcd1234",
                "start_time": i[2],
                "end_time": i[2]+8,
                }

# CREATION DU JSON LIGHTS
for i in fused_data:
    if i[0] == "1":
        for j in range(1,5):
            lig_dict[f"light {j}"][i[1]] = [{
                "device_name": "stu-c100x-abcd1234",
                "channel": 1,
                "start_time": i[2],
                "end_time": i[2]+65,
                }]
            lig_dict[f"light {j}"][i[1]].append({
                "device_name": "stu-c100x-abcd1234",
                "channel": 2,
                "start_time": i[2],
                "end_time": i[2]+65,
                })
    elif i[0] == "2":
        for j in range(5,11):
            if j == 5 or j == 10 :
                lig_dict[f"light {j}"][i[1]] = {
                    "device_name": "stu-c100x-abcd1234",
                    "channel":1,
                    "start_time": i[2],
                    "end_time": i[2]+8,
                    }
            else :
                lig_dict[f"light {j}"][i[1]] = [{
                    "device_name": "stu-c100x-abcd1234",
                    "channel":1,
                    "start_time": i[2],
                    "end_time": i[2]+65,
                    }]
                lig_dict[f"light {j}"][i[1]].append({
                    "device_name": "stu-c100x-abcd1234",
                    "channel":2,
                    "start_time": i[2],
                    "end_time": i[2]+65,
                    })
                
# SAUVEGARDE DES JSON POST

bar_file = open("dev/data_post/barriers.json", "w")
json.dump(bar_dict, bar_file, indent= 6)
bel_file = open("dev/data_post/bells.json", "w")
json.dump(bel_dict, bel_file, indent= 6)
lig_file = open("dev/data_post/lights.json", "w")
json.dump(lig_dict, lig_file, indent= 6)

bar_file.close()
bel_file.close()
lig_file.close()