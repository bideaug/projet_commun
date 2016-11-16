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

Nouvelle_partie = True
if Nouvelle_partie == True :
    Nouvelle_partie = Creation_partie()

def Creation_partie() :
    nombre_de_joueur = input("entrer le nombre de joueur s'il vous plait (max 4): \n")
    nombre_de_joueur_a_creer=nombre_de_joueur
    while nombre_de_joueur_a_creer > 0 :
        joueur_numero = nombre_de_joueur-nombre_de_joueur_a_creer +1
        if joueur_numero == 1:
            nom = raw_input('rentrer votre nom joueur 1 : ')
            joueur_1 = Joueur(nom,0)
        elif joueur_numero == 2:
            nom = raw_input('rentrer votre nom joueur 2 : ')
            joueur_2 = Joueur(nom,0)
        elif joueur_numero == 3:
            nom = raw_input("rentrer votre nom joueur 3 : ")
            joueur_3 = Joueur(nom,0)
        elif joueur_numero == 4:
            nom = raw_input("rentrer votre nom joueur 4 : ")
            joueur_4 = Joueur(nom,0)
        nombre_de_joueur_a_creer = nombre_de_joueur_a_creer -1
    Nouvelle_partie=False
    return Nouvelle_partie

    print("C'est a ",nom_joueur," de lancer les des ! ")
    de_1 = input("Rentrer votre 1er des\n")
    de_2 = input("Rentrer votre 2eme des\n")
    de_3 = input("Rentrer votre 3eme des\n")
    test_1=Chouette(de_1, de_2, de_3)
    test_2=Velute(de_1, de_2, de_3)
    is_a_chouette = Chouette.__is_Chouette__(test_1)
    is_a_velute = Velute.__is_Velute__(test_2)
    test_3=Chouette_Velute()
    is_a_chouette_velute=Chouette_Velute.__is_Chouette_Velute__(test_3, is_a_chouette, is_a_velute)
    if is_a_chouette_velute == True :
        print("is a chouette : ",is_a_chouette)
        print("is a velute : ",is_a_velute)
        print("is a chouette velute : ++ ",is_a_chouette_velute)
    elif is_a_chouette == True:
        print("is a chouette ++ : ",is_a_chouette)
        print("is a velute : ",is_a_velute)
        print("is a chouette velute : ",is_a_chouette_velute)
    elif is_a_velute == True :
        print("is a chouette : ",is_a_chouette)
        print("is a velute ++ : ",is_a_velute)
        print("is a chouette velute : ",is_a_chouette_velute)
    else :
        print("Pas de point marquer !!")
    return Gagnant

Terminer = False
Gagnant = False
while Terminer == False :
#test=Figure(de_1, de_2, de_3)
    deroulement_manche = 1
    while deroulement_manche < nombre_de_joueur+1 :
        if Gagnant == False :
            manche(deroulement_manche)
        deroulement_manche=deroulement_manche+1

"""

class chouette_velute(Chouette, Velute):
    def __init__(self, is_Chouette, is_Velute):
        self.is_Chouette_velute = False
        Chouette.__init__(self, is_Chouette)
        Velute.__init__(self, is_Velute)

    def __is_Chouette_velute__(self, is_Chouette, is_Velute):
        if is_Chouette == is_Velute and is_Chouette == True :
            self.is_Chouette_velute = True
        else:
            self.is_Chouette_velute = False
        return self.is_Chouette_velute


de_1 = input("Rentrer votre 1er des\n")
de_2 = input("Rentrer votre 2eme des\n")
de_3 = input("Rentrer votre 3eme des\n")

jet_1=Chouette()
is_a_chouette = Chouette.__is_Chouette__(jet_1, de_1, de_2, de_3)
print("is_a_chouette",is_a_chouette)

test1=Velute()
is_a_velute = Velute.__is_velute__(test1, de_1, de_2, de_3)
print("is_a_velute : ",is_a_velute)

test2=chouette_velute(is_a_chouette, is_a_velute)
#is_a_chouette_velute=chouette_velute.__is_Chouette_velute__(is_a_chouette, is_a_velute)
is_a_chouette_velute=chouette_velute.__is_Chouette_velute__()
print("is_a_chouette_velute : ",is_a_chouette_velute)
"""
