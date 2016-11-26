#! /usr/bin/python2.7
# -*- coding:utf-8 -*-

import os
import jeu_vocabulaire_function as fpj

nombre_de_fois = 1
test_valide = False

print("***********************************************************************")
print("            Bienvenue dans le jeu pour apprendre l'allemand            ")
print("***********************************************************************")

nom_utilisateur = raw_input("Quel est votre nom ? ")


while test_valide == False :
    nombre_de_fois=fpj.choix_niveau(nombre_de_fois)
    niveau = raw_input()
    var_ok = fpj.test_niveau(niveau)
    if var_ok :
        test_valide=fpj.ouverture_du_niveau(niveau,var_ok)

print("Le niveau selectionner contient : ",nb_de_mot_du_niveau,".")
print("Combien de mot voulez vous avoir ? 0 toute la liste")

