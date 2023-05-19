from pydantic import BaseModel

# Classes for the 3 types of sensors
class Barrier(BaseModel):
   device_name : str
   start_time : float = 0
   start_angle : float = 0
   end_time : int = 0
   end_angle : int = 0
   status : str = "inactive"
   
   def update_barrier(self, new_values : dict):
      self.start_time = new_values['start_time']
      self.end_time = new_values['end_time']
      self.start_angle = new_values['start_angle']
      self.end_angle = new_values['end_angle']
      return self
      
   def update_barrier_status(self):
      if self.start_angle - self.end_angle > 0 and self.end_angle == 0 :
         self.status = "down"
      elif self.start_angle - self.end_angle < 0 and self.end_angle == 90 :
         self.status = "up"
      else :
         self.status = "irregular"
        
class Bell(BaseModel):
   device_name : str
   start_time : int = 0
   end_time : int = 0
   
   def update_bell(self, new_values : dict):
      self.start_time = new_values['start_time']
      self.end_time = new_values['end_time']
   
class Light(BaseModel):
   device_name : str
   start_time : int = 0
   end_time : int = 0
   
   def update_light(self, new_values : dict):
      self.start_time = new_values['start_time']
      self.end_time = new_values['end_time']
   
#######################################################
# Instanciates the 3 sensors classes

def instanciate_sensors ():
   sensors = sensors_dict
   for barrier in sensors.keys():
      sensors[barrier]["cur"]= Barrier(device_name=barrier)
      sensors[barrier]["prev"]= Barrier(device_name=barrier)
      for light in sensors[barrier]["associated_light"]:
         sensors[barrier]["associated_light"][light]= Light(device_name=light)
      for bell in sensors[barrier]['associated_bell']:
         sensors[barrier]['associated_bell'][bell]= Bell(device_name=bell)
   return sensors

#######################################################
# Raw_data needed everytime

sensors_dict = {
      "bar-c100x-abcd1234": {"cur": "", "prev" : "", 
            "associated_light": {"lig-l500X-abcd1234": "", "lig-l500X-efgh2345": ""},
            "associated_bell": {"bel-z200X-abcd1234": ""}
            },
      "bar-c100x-efgh2345": {"cur": "", "prev" : "", 
            "associated_light": {"lig-l500X-ijkl3456": "", "lig-l500X-mnop4567": ""},
            "associated_bell": {"bel-z200X-efgh2345": ""}
            },
      "bar-c100x-ijkl3456": {"cur": "","prev" : "", 
            "associated_light": {"lig-l500X-qrst5678": "", "lig-l500X-uvwx6789": "", "lig-l500X-yzab7890": ""},
            "associated_bell": {"bel-z200X-ijkl3456": ""}
            },
      "bar-c100x-mnop4567": {"cur": "", "prev": "",
            "associated_light": {"lig-l500X-cdef8901": "", "lig-l500X-ghij9012": "", "lig-l500X-klmn0123": ""},
            "associated_bell": {"bel-z200X-mnop4567": ""}
            }
      }

associated_barriers = {'lig-l500X-abcd1234' : "bar-c100x-abcd1234",
                       'lig-l500X-efgh2345' : "bar-c100x-abcd1234",
                       'lig-l500X-ijkl3456' :"bar-c100x-efgh2345",
                        'lig-l500X-mnop4567': "bar-c100x-efgh2345",
                        'lig-l500X-qrst5678': "bar-c100x-ijkl3456",
                        'lig-l500X-uvwx6789': "bar-c100x-ijkl3456",
                        'lig-l500X-yzab7890': "bar-c100x-ijkl3456",
                        'lig-l500X-cdef8901': "bar-c100x-mnop4567",
                        'lig-l500X-ghij9012': "bar-c100x-mnop4567",
                        'lig-l500X-klmn0123': "bar-c100x-mnop4567"    
}

