from pydantic import BaseModel

class Barrier(BaseModel):
   device_name : str
   start_time : int
   start_angle : int
   end_time : int
   end_angle :int
   
class Bell(BaseModel):
   device_name :str
   start_time : int
   end_time : int
   
class Light(BaseModel):
   device_name :str
   channel : str
   start_time : int
   end_time : int

    
# Database creation
bar_dict= dict([(f"barrier {i}", {}) for i in range (1,5)])
bel_dict= dict([(f"bell {i}", {}) for i in range (1,5)])
lig_dict= dict([(f"light {i}", {}) for i in range (1,10)])
db = dict(zip(['barriers', 'bells', 'lights'], [bar_dict,bel_dict,lig_dict])) 