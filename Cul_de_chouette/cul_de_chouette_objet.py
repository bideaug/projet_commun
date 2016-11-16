#! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt
import os.path
import os

class Joueur :
    def __init__(self, nom, score):
        self.nom = nom
        self.score = score

    def __modif_Score__(point):
        score=score+point
        return score

    def __affichage__(self):
        print(self.nom)
        return self.nom

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
        if self.de_1 == self.de_2 :
            self.is_Chouette = True
        elif self.de_1 == self.de_3 :
            self.is_Chouette = True
        elif self.de_2 == self.de_3 :
            self.is_Chouette = True
        else :
            self.is_Chouette = False
        return self.is_Chouette

class Velute(Figure) :

    def __init__(self, de_1, de_2, de_3):
        Figure.__init__(self, de_1, de_2, de_3)
        self.is_Velute = False

    def __is_Velute__(self):
        self.de_1 = int(self.de_1)
        self.de_2 = int(self.de_2)
        self.de_3 = int(self.de_3)
        if self.de_1 + self.de_2 == self.de_3:
            self.is_Velute = True
        elif self.de_1 + self.de_3 == self.de_2:
            self.is_Velute = True
        elif self.de_2 + self.de_3 == self.de_1:
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

