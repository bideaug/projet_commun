#! /usr/bin/python2.7
# -*- coding:utf-8 -*-

import os
import jeu_vocabulaire_function as fpj

nombre_de_fois = 1
test_valide = False

while test_valide == False :
    nombre_de_fois=fpj.choix_niveau(nombre_de_fois)
    niveau = input()
    niveau = int(niveau)
    var_ok = fpj.test_niveau(niveau)
    test_valide=fpj.ouverture_du_niveau(niveau,var_ok)

