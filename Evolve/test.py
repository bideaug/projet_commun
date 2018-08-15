import numpy as np
import os
import time
from component import *
from display_component import *
from forces import *
from variables import *


n0=Node(0,1,0,0,0,[5.,5.])
n1=Node(1,1,0,0,0,[1.,5.])
n2=Node(2,1,0,0,0,[1.,7.])
n3=Node(3,1,0,0,0,[1.,0])
n4=Node(4,1,0,0,0,[-0,6])

m1 = Muscle([n0,n1],10000.)
m2 = Muscle([n1,n2],10000.)
#m3 = Muscle([n2,n3],10000.)
#m4 = Muscle([n2,n4],10000.)
#m5 = Muscle([n3,n4],10000.)


#l0 = Link(n0,n1,m1)
l1 = Link(n1,n0,m1)

l2 = Link(n1,n2,m2)
l3 = Link(n2,n1,m2)
#
#l4 = Link(n2,n3,m3)
#l5 = Link(n3,n2,m3)
#
#l6 = Link(n2,n4,m4)
#l7 = Link(n4,n2,m4)
#
#l8 = Link(n3,n4,m5)
#l9 = Link(n4,n3,m5)
#
#n0.add_link(l0)
#
n1.add_link(l1)
n1.add_link(l2)
#
n2.add_link(l3)
#n2.add_link(l4)
#n2.add_link(l6)
#
#n3.add_link(l5)
#n3.add_link(l8)
#
#n4.add_link(l7)
#n4.add_link(l9)
#
#n0.add_force(Weight(n0))
#n0.add_force(Friction(n0))
#n0.add_force(Support(n0))
#n1.add_force(Support(n1))
#n2.add_force(Support(n2))
#n3.add_force(Support(n3))
#n4.add_force(Support(n4))

n1.add_force(Weight(n1))
n1.add_force(Friction(n1))

n2.add_force(Weight(n2))
n2.add_force(Friction(n2))
#
#n3.add_force(Weight(n3))
#n3.add_force(Friction(n3))
#
#n4.add_force(Weight(n4))
#n4.add_force(Friction(n4))

n1.add_force(Spring_action(n1,n1.get_links()[0]))
n1.add_force(Spring_action(n1,n1.get_links()[1]))
n2.add_force(Spring_action(n2,n2.get_links()[0]))
#n2.add_force(Spring_action(n2,n2.get_links()[1]))
#n2.add_force(Spring_action(n2,n2.get_links()[2]))
#n3.add_force(Spring_action(n3,n3.get_links()[0]))
#n3.add_force(Spring_action(n3,n3.get_links()[1]))
#n4.add_force(Spring_action(n4,n4.get_links()[0]))
#n4.add_force(Spring_action(n4,n4.get_links()[1]))

Test = Creature([n0,n1,n2],[m1,m2])

Test_anim = Screen(Test)
raw_input("Continuer")
i=0
while True:
    i+=1
    #n0.calculate_acceleration()
    #n0.calculate_next_speed()
    #n0.calculate_next_pos()
    #n0.set_pos(n0.get_next_pos())
    #n0.set_speed(n0.get_next_speed())

    n1.calculate_acceleration()
    n1.calculate_next_speed()
    n1.calculate_next_pos()
    n1.set_pos(n1.get_next_pos())
    n1.set_speed(n1.get_next_speed())
    
    n2.calculate_acceleration()
    n2.calculate_next_speed()
    n2.calculate_next_pos()
    n2.set_pos(n2.get_next_pos())
    n2.set_speed(n2.get_next_speed())
    #
    #n3.calculate_acceleration()
    #n3.calculate_next_speed()
    #n3.calculate_next_pos()
    #n3.set_pos(n3.get_next_pos())
    #n3.set_speed(n3.get_next_speed())
    #
    #n4.calculate_acceleration()
    #n4.calculate_next_speed()
    #n4.calculate_next_pos()
    #n4.set_pos(n4.get_next_pos())
    #n4.set_speed(n4.get_next_speed())

    #n0.recalculate_forces()
    n1.recalculate_forces()
    n2.recalculate_forces()
    #n3.recalculate_forces()
    #n4.recalculate_forces()
    #for f in n.get_forces():
    #    if "Support" in f.get_type() and n.get_y_pos() <=0:
    #        print "support ",f.get_action_vector()
    #        print "y speed ",n.get_y_speed()
    #        time.sleep(0.5)
    #print i
    #time.sleep(time_sampling)
    #print "before", Test_anim.new_pos
    Test_anim.set_creature_pos([])
    #print Test_anim.new_pos
    Test_anim.redraw(i)
    time.sleep(0.3)


