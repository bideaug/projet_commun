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

