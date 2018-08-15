import numpy as np
import evolve
import variables


class Node():
    def __init__(self,index,mass,freq,stand,charge,coordinates):
        

        #################
        #index = index of the node
        #freq = activation frequency of the node
        #stand = standing time of the activated node
        #charge = representation of the action of the node on the others
        #links = table giving the indexes of the node this node is liked to
        #        and the muscle linking the two
        #coordinate = location of the node when appearing
        #################

        self.index = index
        self.freq = freq
        self.mass = mass
        self.stand = stand
        self.charge = charge
        self.forces = []
        self.links = []
        self.coordinates = coordinates
        self.next_coordinates = [None ,None]
        self.activated = False
        self.speed = [0.,0.]
        self.next_speed = [None,None]
        self.acceleration = [0.,0.]

    def get_x_pos(self):
        return self.coordinates[0]

    def get_y_pos(self):
        return self.coordinates[1]

    def get_pos(self):
        return self.coordinates

    def get_charge(self):
        return self.charge

    def get_freq(self):
        return self.freq

    def get_mass(self):
        return self.mass
    
    def get_stand(self):
        return self.stand
    
    def get_links(self):
        return self.links
    
    def get_index(self):
        return self.index

    def set_x_pos(self,new_x):
        self.coordinates[0] = new_x

    def set_y_pos(self,new_y):
        self.coordinates[1] = new_y

    def set_pos(self,new_pos):
        self.coordinates = new_pos

    def set_charge(self,new_charge):
        self.charge = new_charge

    def set_freq(self,new_freq):
        self.freq = new_freq
    
    def set_stand(self,new_stand):
        self.stand = new_stand
    
    def add_link(self,new_link):
        self.links.append(new_link)

    def remove_link(self,old):
        del self.links[old]

    def is_activated(self):
        return self.activated

    def activate(self):
        self.activated = True
    
    def deactivate(self):
        self.activated = False

    def add_force(self,new_force):
        self.forces.append(new_force)
    
    def get_forces(self):
        return self.forces

    def recalculate_forces(self):
        for f in self.forces:
           f.set_action_vector()
    
    def get_x_speed(self):
        return self.speed[0]
    
    def get_y_speed(self):
        return self.speed[1]

    def get_speed(self):
        return self.speed

    def set_speed(self,new_speed):
        self.speed = new_speed

    def set_x_speed(self,new_xspeed):
        self.speed[0] = new_xspeed

    def set_y_speed(self,new_yspeed):
        self.speed[1] = new_yspeed

    def calculate_acceleration(self):
        self.acceleration = [0.,0.]
        for f in self.forces:
            self.acceleration[0]+=f.get_action_vector()[0]
            self.acceleration[1]+=f.get_action_vector()[1]

        self.acceleration[0]=self.acceleration[0]/self.mass
        self.acceleration[1]=self.acceleration[1]/self.mass

    def get_x_acceleration(self):
        return self.acceleration[0]
    
    def get_y_acceleration(self):
        return self.acceleration[1]
    
    def get_acceleration(self):
        return self.acceleration

    def set_speed(self,new_speed):
        self.speed = new_speed
    
    def set_next_speed(self,new_speed):
        self.next_speed = new_speed

    def calculate_next_pos(self):
        self.next_coordinates[0] = self.coordinates[0] + self.speed[0]*variables.time_sampling
        self.next_coordinates[1] = self.coordinates[1] + self.speed[1]*variables.time_sampling

    def calculate_next_speed(self):
        #print "in calc next speed:", self.acceleration
        self.next_speed[0] = self.speed[0] + self.acceleration[0]*variables.time_sampling
        self.next_speed[1] = self.speed[1] + self.acceleration[1]*variables.time_sampling
        #print self.speed
        
    def get_next_pos(self):
        return self.next_coordinates

    def get_next_speed(self):
        return self.next_speed
        
        



class Muscle():
    def __init__(self,nodes,hardness,*length):
        self.nodes = nodes
        self.hardness = hardness
        if length in locals():
            self.length = length[0]
        else:
            self.length =  np.sqrt((self.nodes[0].get_pos()[0]-self.nodes[1].get_pos()[0])**2 + (self.nodes[0].get_pos()[1]-self.nodes[1].get_pos()[1])**2)

    def get_nodes(self):
        return self.nodes

    def get_hardness(self):
        return self.hardness

    def get_length(self):
        return self.length



class Link():
    def __init__(self,node_1,node_2,muscle):
        self.node_1 = node_1
        self.node_2 = node_2
        self.muscle = muscle
    def get_nodes(self):
        return self.node_1,self.node_2
    def get_muscle(self):
        return self.muscle
    def calculate_distance(self):
        return np.sqrt((self.node_1.get_pos()[0]-self.node_2.get_pos()[0])**2 + (self.node_1.get_pos()[1]-self.node_2.get_pos()[1])**2)
        



class Creature():
    def __init__(self,nodes = None, muscles=None, *ancestor):
        
        if nodes != None and muscles != None: 
            self.nodes = nodes
            self.muscles = muscles
        else:
            best_nodes_number = variables.get_best_nodes_number()
            nodes_number = int(np.abs(np.random.randn())+best_nodes_number)
            print "nodes number:", nodes_number

            self.nodes=[]
            self.muscles = []

            for i in np.arange(nodes_number):
                freq_av = variables.get_freq_average()
                freq_node = int(np.abs(np.random.randn())+freq_av)
                mass_av = variables.get_mass_average()
                mass_node = np.abs(mass_av * np.random.randn())
                print "mass ",i,": ", mass_node

                stand_av = variables.get_stand_average()
                stand_node = int(np.abs(np.random.randn())+stand_av)

                charge_av = variables.get_charge_average()
                charge_node = int(np.abs(np.random.randn())+charge_av)
                

                coordinates_node = [5*np.abs(np.random.randn()),5*np.abs(np.random.randn())]
                self.nodes.append(Node(i,mass_node,freq_node,stand_node,charge_node,coordinates_node))
                
            neighboors_av = variables.get_neighboors_average()
            self.neighboors_table = np.zeros((nodes_number,nodes_number),dtype = int)


            
            for n in np.arange(nodes_number):
                neighboors_number = int(np.abs(np.random.randn()+neighboors_av))
                print "neighboors ",i,": ", neighboors_number
                if neighboors_number == 0:
                    neighboors_number += 1
                
                if neighboors_number < np.sum(self.neighboors_table[n]):
                    neighboors_number = np.sum(self.neighboors_table[n])



                for i in np.arange(neighboors_number)-np.sum(self.neighboors_table[n]):
                    
                    while True:
                        new_neighboor = np.random.random_integers(0,nodes_number-1)

                        if list(self.neighboors_table[n])[new_neighboor] == 0 and n!= new_neighboor:
                            self.neighboors_table[n][new_neighboor] = 1
                            self.neighboors_table[new_neighboor][n] = 1
                            break
                for i in np.arange(nodes_number):
                    self.neighboors_table[i][0:i+1] = 0



            hardness_av = variables.get_hardness_average()
            for n in self.nodes:
                #print "coucou"
                for i in np.arange(len(self.neighboors_table[n.get_index()])):
                    if self.neighboors_table[n.get_index()][i] == 1:
                        hardness_muscle = hardness_av*np.random.randn()+hardness_av
                        for nn in self.nodes:
                            if nn.get_index() == i:
                                n2 = nn
                                break
                        muscle = Muscle([n,n2],hardness_muscle)
                        link = Link(n,n2,muscle)
                        link2 = Link(n2,n,muscle)
                        n.add_link(link)
                        n2.add_link(link2)
                        self.muscles.append(muscle)

    def get_nodes(self):
        return self.nodes

    def get_muscles(self):
        return self.muscles
    
    def get_neighboors_table(self):
        return self.neighboors_table



#    def evolve(self):
        
