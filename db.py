from pydantic import BaseModel

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
      self.status = new_status
   
   def update_barrier(self, new_values : dict):
      self.start_time = new_values['start_time']
      self.end_time = new_values['end_time']
      self.start_angle = new_values['start_angle']
      self.end_angle = new_values['end_angle']
      
   def update_barrier_status(self):
      if self.start_angle - self.end_angle > 0 and self.end_angle == 0 :
         self.change_status("down")
      elif self.start_angle - self.end_angle < 0 and self.end_angle == 90 :
         self.change_status("up")
      else :
         self.change_status("irregular")
      
class Bell(BaseModel):
   device_name : str
   start_time : int = 0
   end_time : int= 0
   
   def update_bell(self, new_values : dict):
      self.start_time = new_values['start_time']
      self.end_time = new_values['end_time']
   
class Light(BaseModel):
   device_name : str
   start_time : int= 0
   end_time : int= 0
   
   def update_light(self, new_values : dict):
      self.start_time = new_values['start_time']
      self.end_time = new_values['end_time']
   

captors_dict = {
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

# Instanciates the 3 captors classes

def instanciate_captors ():
   captors = captors_dict
   for barrier in captors.keys():
      captors[barrier]["cur"]= Barrier(device_name=barrier)
      captors[barrier]["prev"]= Barrier(device_name=barrier)
      for light in captors[barrier]["associated_light"]:
         captors[barrier]["associated_light"][light]= Light(device_name=light)
      for bell in captors[barrier]['associated_bell']:
         captors[barrier]['associated_bell'][bell]= Bell(device_name=bell)
   return captors