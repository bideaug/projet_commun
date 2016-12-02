import os
import numpy as np
import make_dir
import threading
from scipy import ndimage
import matplotlib.pyplot as plt

global user_path
global path_to_diec
global index_max
global index_min
verification = True
while verification :
    try :
        index_min = input("Entrer la valeur minimale\n")
        index_max = input("Entrer la valeur maximale\n")
        verification = False
    except:
        verification = True

class Pic_Thread(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.Stop=False
        self.pic_index=0
        self.i=0

    def run(self):
        self.set_pic_index()
        self.fichier = user_path + "/" + str(self.pic_index)+".png"
        self.pic = ndimage.imread(self.fichier)
        plt.imshow(self.pic)
        plt.show()
        while not self.Stop:
            self.i+=1
    
    def update(self):
        self.set_pic_index()
        self.fichier = user_path + "/" + str(self.pic_index)+".png"
        self.pic = ndimage.imread(self.fichier)
        plt.imshow(self.pic)
        plt.show()

    def get_pic_index(self):
        return self.pic_index

    def set_pic_index(self):
        self.pic_index = np.random.random_integers(index_min,index_max)
    
    def stop(self):
        self.Stop = True



user_path,path_to_dic = make_dir.Make_direction()

running = True
picture = Pic_Thread() 
picture.start()

while running:
    verification = True

    while verification:
        try : 
            answer = raw_input("Quel est le nombre correspondant?\n")
            if answer.lower() == "exit":
                verification = False
                running = False
                picture.stop()
                print "END"
                break

            elif int(answer) == picture.get_pic_index() :
                print "CORRECT.\n"
                verification = False
                picture.update()
            else : 
                print "FALSE. Bonne reponse : ", get_pic_index, "\nAppuyez sur enter\n"
                end=raw_input()       
                verification = False
                picture.update()
        except :
            verification = True

    if answer.lower() == "exit":
        break
print "Fermer la fenetre d'image avec ctrl + w"
