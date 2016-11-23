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
    try :
        niveau = int(niveau)
    except :
        print("Rentrer un numéro s'il vous plait")
    var_ok = fpj.test_niveau(niveau)
    test_valide=fpj.ouverture_du_niveau(niveau,var_ok)


