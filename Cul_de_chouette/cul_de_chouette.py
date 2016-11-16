#! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt
import os.path

"""
Je ne sais pas pourquoi je ne peux pas faire passer des Booleen en argument pour la methode de Chouette_velute

Sinon le programme marche pas trop mal mais il faut rajouter quelque chose pour faire en sorte que les nombres pour les 
de soit bien des entier et qu ils soit compris entre 1 et 6

Et rajouter les autres regles et ensuite faire un truc qui permet de les prendre en compte ou pas genre 
Par defaut on active tout et
rentrer les regles que vous ne voulez pas
a = :_
False regle de a
et apres quand on regarde si sa fait un truc ou pas on instantie que les trucs true.
"""

class Chouette : #Definition de la classe Chouette
    """Classe definissant une chouette pas l'analyse des des"""

    def __init__(self):
        self.is_Chouette = False

    def __is_Chouette__(self, de_1, de_2, de_3):
        if de_1 == de_2 :
            self.is_Chouette = True
        elif de_1 == de_3 :
            self.is_Chouette = True
        elif de_2 == de_3 :
            self.is_Chouette = True
        else :
            self.is_Chouette = False
        return self.is_Chouette

class Velute :

    def __init__(self):
        self.is_Velute = False

    def __is_velute__(self, de_1, de_2, de_3):
        if de_1 + de_2 == de_3:
            self.is_Velute = True
        elif de_1 + de_3 == de_2:
            self.is_Velute = True
        elif de_2 + de_3 == de_1:
            self.is_Velute = True
        else :
            self.is_Velute = False
        return self.is_Velute
"""
class chouette_velute():
    def __init__(self):
        self.is_Chouette_velute = False

    def __is_Chouette_velute__(self, is_Chouette, is_Velute) :
        if is_Chouette == is_Velute and is_Chouette == True :
            self.is_Chouette_velute = True
        else:
            self.is_Chouette_velute = False
        return self.is_Chouette_velute
"""

de_1 = input("Rentrer votre 1er des\n")
de_2 = input("Rentrer votre 2eme des\n")
de_3 = input("Rentrer votre 3eme des\n")

jet_1=Chouette()
is_a_chouette = Chouette.__is_Chouette__(jet_1, de_1, de_2, de_3)
print("is_a_chouette",is_a_chouette)

test1=Velute()
is_a_velute = Velute.__is_velute__(test1, de_1, de_2, de_3)
print("is_a_velute : ",is_a_velute)
"""
test2=chouette_velute()
is_a_chouette_velute=chouette_velute.__is_Chouette_velute__(is_a_chouette, is_a_velute)
print("is_a_chouette_velute : ",is_a_chouette_velute)
"""
