import os
import numpy as np
import make_dir
import threading
from scipy import ndimage
import matplotlib.pyplot as plt

class Pic_Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.Stop=False
    def run(self):
        try :
            self.fichier = user_path + "/" + str(index)+".png"
            self.pic = ndimage.imread(self.fichier)
            plt.imshow(self.pic)
            plt.show()
            while True:
                if self.Stop:
                    raise ValueError ("EOT")
        except :
            print ""
    def stop(self):
        self.Stop = True
    def stop_and_quit(self):
        exit()


global user_path
global path_to_diec
global index

user_path,path_to_dic = make_dir.Make_direction()

running = True

while running:
    index = np.random.random_integers(0,3)
    picture = Pic_Thread() 
    picture.start()
    verification = True

    while verification:
        try : 
            answer = raw_input("Quel est le nombre correspondant?")
       
            if answer.lower() == "exit":
                verification = False
                running = False
                print "END"
                break

            elif int(answer) == index :
                print "CORRECT.\n"
                verification = False
                picture.stop()

            else : 
                print "FALSE. Bonne reponse : ", index, "\nAppuyez sur enter\n"
                end=raw_input()       
                verification = False
                picture.stop()
        except :
            verification = True

    if answer.lower() == "exit":
        break
    else:
        picture = 0
plt.close()
picture.stop_and_quit()
print "End"
exit()
