import numpy as np
from variables import *
import time

class Force():

    def __init__(self,node):
        self.node=node
        self.action_vector = [None,None]
        self.type = None

    def set_action_vector(self,new_action_vector):
        self.action_vector = new_action_vector

    def get_action_vector(self):
        return self.action_vector

    def get_type(self):
        return self.type
        




class Weight(Force):
    
    def __init__(self,node):
        Force.__init__(self,node)
        self.action_vector = [0,-9.81*self.node.get_mass()]
        self.type = "Weight"

    def set_action_vector(self):
        return None

class Support(Force):
    
    def __init__(self,node):
        Force.__init__(self,node)
        self.type = "Support"
        if self.node.get_pos()[1] <= 0 and self.node.get_y_acceleration()<0:
            self.action_vector = [0.,0.]
            self.action_vector[1] = -self.node.get_y_acceleration()*self.node.get_mass()
            self.node.set_y_speed(0.)
	    
                   
        else:
            self.action_vector = [0.,0.]
            
            

    def set_action_vector(self):
        if self.node.get_pos()[1] <= 0 and self.node.get_y_acceleration()<0:
            self.action_vector = [0.,0.]
            self.action_vector[1] = -self.node.get_y_acceleration()*self.node.get_mass()
            self.node.set_y_speed(0.)

                    
        else:
            self.action_vector = [0.,0.]

class Friction(Force):
    def __init__(self,node):
        Force.__init__(self,node)
        self.viscosity = 0.
        self.type = "Friction"

        self.action_vector[0] = -self.node.get_x_speed()*self.viscosity
        self.action_vector[1] = -self.node.get_y_speed()*self.viscosity

    def set_action_vector(self):

        self.action_vector[0] = -self.node.get_x_speed()*self.viscosity
        self.action_vector[1] = -self.node.get_y_speed()*self.viscosity



class Spring_action(Force):
    def __init__(self,node,link):
        Force.__init__(self,node)
        self.link = link
        self.type = "Spring " + str(node.get_index())

        dir_action = [None,None]
        
        dir_action[0] = self.link.get_nodes()[1].get_pos()[0] - self.link.get_nodes()[0].get_pos()[0]
        dir_action[1] = self.link.get_nodes()[1].get_pos()[1] - self.link.get_nodes()[0].get_pos()[1]
        
        length = self.link.calculate_distance()
        
        dir_action[0] = dir_action[0]/length
        dir_action[1] = dir_action[1]/length
        
        self.action_vector[0] = dir_action[0]*(length-self.link.get_muscle().get_length())*self.link.get_muscle().get_hardness()
        self.action_vector[1] = dir_action[1]*(length-self.link.get_muscle().get_length())*self.link.get_muscle().get_hardness()
   
    def set_action_vector(self):
        dir_action = [None,None]
        
        dir_action[0] = self.link.get_nodes()[1].get_pos()[0] - self.link.get_nodes()[0].get_pos()[0]
        dir_action[1] = self.link.get_nodes()[1].get_pos()[1] - self.link.get_nodes()[0].get_pos()[1]
        
        length = self.link.calculate_distance()
        
        dir_action[0] = dir_action[0]/length
        dir_action[1] = dir_action[1]/length
        
        self.action_vector[0] = dir_action[0]*(length-self.link.get_muscle().get_length())*self.link.get_muscle().get_hardness()
        self.action_vector[1] = dir_action[1]*(length-self.link.get_muscle().get_length())*self.link.get_muscle().get_hardness()
        
