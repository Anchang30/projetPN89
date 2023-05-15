import os

class PN :
    
    # set root_path to : '/home/vincent/projetPN89'
    root_path = os.path.dirname(__file__)

        
    def get_barrier_data(self):
        barrier_path = os.path.join(self.root_path,"data","barrier_files")
        barrier_files = [f for f in os.listdir(barrier_path) if f.endswith(".json")]
        return barrier_files, barrier_path
        
    def get_bell_data(self):
        bell_path = os.path.join(self.root_path,"data","bell_files")
        bell_files = [f for f in os.listdir(bell_path) if f.endswith(".json")]
        return bell_files, bell_path
    
    def get_light_data(self):
        light_path = os.path.join(self.root_path,"data","light_files")
        light_files = [f for f in os.listdir(light_path) if f.endswith(".json")]
        return light_files, light_path
    

    def ping(self):
        """
        You call ping I print pong.
        """
        print("ping-pong")