#! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt
import os.path
import os
import cul_de_chouette_objet as obj



def Lancer_de_de(n_du_de):
    is_de_ok = False
    if n_du_de == 1 :
        while is_de_ok == False :
            print("Rentrer la valeur du ",n_du_de," er de")
            de = raw_input()
            is_de_ok = Verificateur_de_des(de)
    if n_du_de == 2 or n_du_de == 3 :
        while is_de_ok == False :
            print("Rentrer la valeur du ",n_du_de," eme de")
            de = raw_input()
            is_de_ok = Verificateur_de_des(de)
    return de

def Verificateur_de_des(de) :
    i = 1
    is_ok = False
    de = int(de)
    while i < 7:
        if i == de :
            is_ok = True
            return is_ok
        i = i+1
    return is_ok


def is_figure(is_a_chouette_velute, is_a_chouette, is_a_velute):
    selecteur = 0
    if is_a_chouette_velute == True :
        print("is a chouette : ",is_a_chouette)
        print("is a velute : ",is_a_velute)
        print("is a chouette velute : ++ ",is_a_chouette_velute)
        selecteur = 3
    elif is_a_chouette == True:
        print("is a chouette ++ : ",is_a_chouette)
        print("is a velute : ",is_a_velute)
        print("is a chouette velute : ",is_a_chouette_velute)
        selecteur = 1
    elif is_a_velute == True :
        print("is a chouette : ",is_a_chouette)
        print("is a velute ++ : ",is_a_velute)
        print("is a chouette velute : ",is_a_chouette_velute)
        selecteur = 2
    else :
        print("Pas de point marquer !!")
        selecteur = 0
    return selecteur

def Tour_de_jeu(joueur):
    is_a_chouette = False
    is_a_velute = False
    is_a_chouette_velute = False
    de_1 = Lancer_de_de(1)
    de_2 = Lancer_de_de(2)
    de_3 = Lancer_de_de(3)
    test_chouette = obj.Chouette(de_1, de_2, de_3)
    test_velute = obj.Velute(de_1, de_2, de_3)
    is_a_chouette = test_chouette.__is_Chouette__()
    is_a_velute = test_velute.__is_Velute__()
    test_chouette_velute=obj.Chouette_Velute()
    is_a_chouette_velute=test_chouette_velute.__is_Chouette_Velute__(is_a_chouette, is_a_velute)
    selecteur_de_figure=is_figure(is_a_chouette_velute,is_a_chouette,is_a_velute)
    print(selecteur_de_figure)
