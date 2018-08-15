import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
import variables

class Screen():
    def __init__(self,creature):
        self.fig=plt.figure()
        self.ax=self.fig.add_subplot(111,aspect = 'equal')
        self.creature = creature
        self.circles_n = []
        self.lines_m = []
        self.lines_acc = []
        self.new_pos = []

        for n in self.creature.get_nodes():
            self.circles_n.append(plt.Circle(n.get_pos(),radius = 0.1,color = 'black'))
            self.ax.add_artist(self.circles_n[-1])
            
            self.lines_acc.append(mlines.Line2D([n.get_x_pos(),n.get_x_pos()+n.get_x_acceleration()*0.1],[n.get_y_pos(),n.get_y_pos()+n.get_y_acceleration()*0.1],color='red'))
            self.ax.add_line(self.lines_acc[-1])

        for m in self.creature.get_muscles():
            self.lines_m.append(mlines.Line2D([m.get_nodes()[0].get_pos()[0],m.get_nodes()[1].get_pos()[0]],[m.get_nodes()[0].get_pos()[1],m.get_nodes()[1].get_pos()[1]]))
            self.ax.add_line(self.lines_m[-1])
        self.text = self.ax.text(10,10,"t = 0")

        plt.plot()
        plt.show(block = False)
    
    def get_circles_n(self):
        return self.circles_n

    def get_lines_m(self):
        return self.lines_m
    
    def set_circles_n_pos(self,new_n_pos):
        for i in np.arange(len(self.circles_n)):
            self.circles_n[i].center = new_n_pos[i]
    
    def set_lines_m_pos(self,new_m_pos):
        for i in np.arange(len(self.lines_m)):
            self.lines_m[i].set_xdata(new_m_pos[i][0])
            self.lines_m[i].set_ydata(new_m_pos[i][1])

    def set_creature_pos(self,new_creature_pos):
        self.new_creature_pos = new_creature_pos

        print self.new_creature_pos

        if len(self.new_creature_pos) ==0:
            for n in self.creature.get_nodes():
                #print "coucou oui"
                self.new_creature_pos.append(n.get_pos())
                
                self.lines_acc[n.get_index()].set_xdata([n.get_pos()[0],n.get_x_pos()+n.get_x_acceleration()*0.1])
                self.lines_acc[n.get_index()].set_ydata([n.get_pos()[1],n.get_y_pos()+n.get_y_acceleration()*0.1])
        #print "coucou ouii 2"
        #print self.new_creature_pos
        self.set_circles_n_pos(self.new_creature_pos)
        
        for m in self.creature.get_muscles():
           self.lines_m[self.creature.get_muscles().index(m)].set_xdata([m.get_nodes()[0].get_pos()[0],m.get_nodes()[1].get_pos()[0]])
           self.lines_m[self.creature.get_muscles().index(m)].set_ydata([m.get_nodes()[0].get_pos()[1],m.get_nodes()[1].get_pos()[1]])



    def redraw(self,time):
        #print self.ax.relim()

        #self.ax.relim()
        #self.ax.autoscale_view()
        self.ax.set_ylim([-10,10])
        self.ax.set_xlim([-5,15])
        self.text.set_text("t = "+str(time*variables.time_sampling))
        self.fig.canvas.draw()
        #print "in redraw ",self.new_pos
        

