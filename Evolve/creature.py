from component import *
import numpy as np
import variables
import evolve

class Creature():
    def __init__(self,*ancestor):
        self.nodes = []
        self.muscles = []
        
        #if ancestor in locals():
        #    self.nodes,self.muscles = ancestor.evolve()
        #else:
        if True:
            best_nodes_number = variables.get_best_nodes_number()
            nodes_number = int(np.abs(np.random.randn())+best_nodes_number)

            self.nodes=[]

            for i in np.arange(nodes_number):
                freq_av = variables.get_freq_average()
                freq_node = int(np.abs(np.random.randn())+freq_av)

                stand_av = variables.get_stand_average()
                stand_node = int(np.abs(np.random.randn())+stand_av)

                charge_av = variables.get_charge_average()
                charge_node = int(np.abs(np.random.randn())+charge_av)
                

                coordinates_node = [5*np.abs(np.random.randn()),5*np.abs(np.random.randn())]
                self.nodes.append(Node(i,freq_node,stand_node,charge_node))
                
            neighboors_av = variables.get_neighboors_average()
            self.neighboors_table = np.zeros((nodes_number,nodes_number),dtype = int)


            
            for n in np.arange(nodes_number):
                neighboors_number = int(np.abs(np.random.randn()+neighboors_av))
                if neighboors_number == 0:
                    neighboors_number += 1
                
                if neighboors_number < np.sum(self.neighboors_table[n]):
                    neighboors_number = np.sum(self.neighboors_table[n])



                for i in np.arange(neighboors_number)-np.sum(self.neighboors_table[n]):
                    
                    while True:
                        new_neighboor = np.random.random_integers(0,nodes_number-1)

                        if list(self.neighboors_table[n])[new_neighboor] == 0 and n!= new_neighboor:
                            self.neigboors_table[n][new_neighboor] = 1
                            self.neigboors_table[new_neighboor][n] = 1
                            break
                for i in np.arange(nodes_number):
                    self.neighboors_table[i][0:i+1] = 0



            hardness_av = variables.get_hardness_average()
            for n in self.nodes:
                for i in self.neighboors_table[n.get_index()]:
                    if i == 1:
                        hardness_muscle = int(np.abs(np.random.randn())+muscle_av)
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

    def get_nodes():
        return self.nodes

    def get_muscles():
        return self.muscles
                        


#    def evolve(self):
 
