#! /usr/bin/python2.7
# -*- coding:utf-8 -*-

import os

def choix_niveau(nombre_de_fois) :
    """
Cette fonction demande le niveau que le joueur veux travailler.
    """
    if nombre_de_fois == 1 :  
        print("Quel niveau voulez vous travailler, tapper le numéro correspondant ?\n niveau 1 : 1\n niveau 2 : 2\n niveau 3 :3 \n niveau 4 :4\n")
    else :
        print("Veuiller rentrer le nouveau niveau que vous souhaitez travailler, tapper le numéro correspondant ?\n niveau 1 : 1\n niveau 2 : 2\n niveau 3 :3 \n niveau 4 :4\n")
    nombre_de_fois=nombre_de_fois+1
    return nombre_de_fois

def test_niveau(variable_a_tester) :
    """ 
Cette fonction test l'entrer du joueur et vérifie que c'est bien un entier en 1 et 4    
    """
    if (variable_a_tester > 0 and variable_a_tester < 5) :
        variable_ok = True
    else :
        variable_ok = False

    return variable_ok #renvoi vrai si la variable est ok sinon renvoit faux

def ouverture(niveau,ouvert) :
    """
Cette fonction ouvre le fichier du niveau que le joueur à demander si ouvert est VRAI
si ouvert est FAUX elle ferme le fichier en question

Cette fonction ne renvoit aucune valeur pour le moment
    """
    if ouvert :
        if niveau == 1 :
                voca_liste = open("./vocabulaire_liste/vocab_lvl_1", "r")
        elif niveau == 2 :
                voca_liste = open("./vocabulaire_liste/vocab_lvl_2", "r")
        elif niveau == 3 :
                voca_liste = open("./vocabulaire_liste/vocab_lvl_3", "r")
        else :
                voca_liste = open("./vocabulaire_liste/vocab_lvl_4", "r")
    else :
        voca_liste.close()
    return 0

def ouverture_du_niveau(niveau,var_ok) :
    """
Cette fonction fait ouvrir le fichier l'entrer du joueur était consistante et renvoi test=True sinon elle renvoit test=False
    """
    if var_ok :
        ouverture(niveau,True)
        test=True
    else :
        print("Vous n'avez pas rentrer ce qu'il fallait\n\n")
        test=False
    return  test


