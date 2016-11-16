#! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt
import os.path
import os

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
class Joueur :
    def __init__(self, nom, score):
        self.nom = nom
        self.score = score

    def __modif_Score__(point):
        score=score+point
        return score

    def __str__(self):
        print(self.nom)

class Figure :
    
    def __init__(self, de_1, de_2, de_3):
        self.de_1 = de_1
        self.de_2 = de_2
        self.de_3 = de_3

class Chouette(Figure) : #Definition de la classe Chouette
    """Classe definissant une chouette pas l'analyse des des"""

    def __init__(self, de_1, de_2, de_3):
        Figure.__init__(self, de_1, de_2, de_3)
        self.is_Chouette = False

    def __is_Chouette__(self):
        if de_1 == de_2 :
            self.is_Chouette = True
        elif de_1 == de_3 :
            self.is_Chouette = True
        elif de_2 == de_3 :
            self.is_Chouette = True
        else :
            self.is_Chouette = False
        return self.is_Chouette

class Velute(Figure) :

    def __init__(self, de_1, de_2, de_3):
        Figure.__init__(self, de_1, de_2, de_3)
        self.is_Velute = False

    def __is_Velute__(self):
        if de_1 + de_2 == de_3:
            self.is_Velute = True
        elif de_1 + de_3 == de_2:
            self.is_Velute = True
        elif de_2 + de_3 == de_1:
            self.is_Velute = True
        else :
            self.is_Velute = False
        return self.is_Velute

class Chouette_Velute() :
    def __init__(self):
        self.is_Chouette_Velute = False
        #self.is_Chouette = is_Chouette
        #self.is_Velute = is_Velute

    def __is_Chouette_Velute__(self,is_Chouette, is_Velute):
        if is_Chouette and is_Chouette == is_Velute :
            self.is_Chouette_Velute = True
        else :
            self.is_Chouette_Velute = False
        return self.is_Chouette_Velute

