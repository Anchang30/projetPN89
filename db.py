from pydantic import BaseModel

captor_dict = {"captor_list" : {"barrier_list" : 
    ["bar-c100x-abcd1234", "bar-c100x-efgh2345", "bar-c100x-ijkl3456", "bar-c100x-mnop4567"],
"bell_list" : 
    ["bel-z200X-abcd1234", "bel-z200X-efgh2345", "bel-z200X-ijkl3456", "bel-z200X-mnop4567"],
"light_list" : ["lig-l500X-abcd1234", "lig-l500X-efgh2345", "lig-l500X-ijkl3456", "lig-l500X-mnop4567",
    "lig-l500X-qrst5678", "lig-l500X-uvwx6789", "lig-l500X-yzab7890", "lig-l500X-cdef8901"],
"single_lights": ["lig-l500X-ghij9012", "lig-l500X-klmn0123"]}}

# Classes pour les 3 types de capteurs

class Barrier(BaseModel):
   device_name : str
   start_time : int= 0
   start_angle : int= 0
   end_time : int= 0
   end_angle : int= 0
   status : str = "inactive"
   
   def change_status(self, new_status : str):
      new_status = new_status.lower()
      list_of_status = ["inactive","up", "down", "irregular"]
      if new_status not in list_of_status :
         print ("This status is unknown")
      self.curr_status = new_status
   
   def update_barrier(self, new_values : dict):
      self.start_time = new_values['start_time']
      self.end_time = new_values['end_time']
      self.start_angle = new_values['start_angle']
      self.end_angle = new_values['end_angle']
      
class Bell(BaseModel):
   device_name : str
   start_time : int = 0
   end_time : int= 0
   
   def update_bell(self, new_values : dict):
      self.start_time = new_values['start_time']
      self.end_time = new_values['end_time']
   
class Light(BaseModel):
   device_name : str
   channel : int 
   start_time : int= 0
   end_time : int= 0
   
   def update_light(self, new_values : dict):
      self.start_time = new_values['start_time']
      self.end_time = new_values['end_time']
   
# Instanciates the 3 captors classes

def instanciate_captors ():
   barriers = {}
   bells = {} 
   lights = {}
   
   for captor in captor_dict['captor_list']['barrier_list']:
      barriers[f"{captor}_cur"] = Barrier(device_name = captor)
      barriers[f"{captor}_pre"] = Barrier(device_name = captor)
   
   for captor in captor_dict['captor_list']['bell_list']:
      bells[f"{captor}_cur"] = Bell(device_name = captor)
      bells[f"{captor}_pre"] = Bell(device_name = captor)
      
   for num, captor in enumerate(captor_dict['captor_list']['light_list']):
      lights[f"{captor}_cur"] = Light(device_name = captor, channel = 2 if num%2 ==1 else 1)
      lights[f"{captor}_pre"] = Light(device_name = captor, channel = 2 if num%2 ==1 else 1)
   
   lights[f"{captor_dict['captor_list']['single_lights'][0]}_cur"] = \
      Light(device_name = captor_dict['captor_list']['single_lights'][0], channel = 1)
   lights[f"{captor_dict['captor_list']['single_lights'][0]}_pre"] = \
      Light(device_name = captor_dict['captor_list']['single_lights'][0], channel = 1)
   lights[f"{captor_dict['captor_list']['single_lights'][1]}_cur"] = \
      Light(device_name = captor_dict['captor_list']['single_lights'][0], channel = 1)
   lights[f"{captor_dict['captor_list']['single_lights'][1]}_pre"] = \
      Light(device_name = captor_dict['captor_list']['single_lights'][0], channel = 1)
   
   return {"captor_list" : {"barriers": barriers, "bells": bells, "lights": lights}}