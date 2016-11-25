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


#def is_figure(is_a_chouette_velute, is_a_chouette, is_a_velute):
    #selecteur = 0
    #if is_a_chouette_velute == True :
        #print("is a chouette : ",is_a_chouette)
        #print("is a velute : ",is_a_velute)
        #print("is a chouette velute : ++ ",is_a_chouette_velute)
        #selecteur = 3
    #elif is_a_chouette == True:
        #print("is a chouette ++ : ",is_a_chouette)
        #print("is a velute : ",is_a_velute)
        #print("is a chouette velute : ",is_a_chouette_velute)
        #selecteur = 1
    #elif is_a_velute == True :
        #print("is a chouette : ",is_a_chouette)
        #print("is a velute ++ : ",is_a_velute)
        #print("is a chouette velute : ",is_a_chouette_velute)
        #selecteur = 2
    #else :
        #print("Pas de point marquer !!")
        #selecteur = 0
    #return selecteur

def Chouette(de_1,de_2,de_3):
    if de_1 == de_2 or de_1 == de_3 :
        chouette_de = de_1
    elif de_2 == de_3 :
        chouette_de = de_2
    else :
        chouette_de = int(0)
    return chouette_de

def Cul_de_chouette(de_1,de_2,de_3):
    if de_1 == de_2 and de_2 == de_3 :
        is_cul_de_chouette = de_3
    else :
        is_cul_de_chouette = False
    return is_cul_de_chouette

def Chouette_bleu_rouge(de_1,de_2,de_3):
    if (de_1 == 4 and de_2 == 4 and de_3 == 5) or (de_1 == 5 and de_2 == 4 and de_3 == 4) or (de_1 == 4 and de_2 == 5 and de_3 == 4):
        bleu_rouge = True
    else :
        bleu_rouge = False
    return bleu_rouge

def Velute(de_1,de_2,de_3):
    if de_1 + de_2 == de_3 :
        velute_de = de_3
    elif de_1 + de_3 == de_2 :
        velute_de = de_2
    elif de_2 + de_3 == de_1 :
        velute_de = de_1
    else :
        velute_de = False
    return velute_de


def Figure_and_points(de_1,de_2,de_3):
    points = 0
    is_chouette = Chouette(de_1,de_2,de_3)
    is_velute = Velute(de_1,de_2,de_3)
    if is_chouette :
        is_bleu_rouge = Chouette_bleu_rouge(de_1,de_2,de_3)
        is_chouette_velute = Velute(de_1,de_2,de_3)
        is_cul_de_chouette = Cul_de_chouette(de_1,de_2,de_3)
        #print(is_bleu_rouge)
        #print(is_chouette_velute)
        if is_bleu_rouge :
            points = is_chouette**2
#faire les trucs du bleu rouge
#faire le condition pour les autres chouette special
        elif is_chouette_velute :
            points = 2*(is_chouette**2)
            print("Vous avez gagner les points de la chouette velute")
        elif is_cul_de_chouette : 
            points = 50+(is_cul_de_chouette-1)*10
        else :
            points = is_chouette**2
            print("Vous avez gagner les points de la chouette de ",is_chouette)
    elif is_velute :
        #print(is_velute)
        points = 2*(is_velute**2)
        print("Vous avez gagner les points de la velute")
    return points

def Tour_de_jeu():
    #is_a_chouette = False
    #is_a_velute = False
    #is_a_chouette_velute = False
    de_1 = Lancer_de_de(1)
    de_2 = Lancer_de_de(2)
    de_3 = Lancer_de_de(3)
    de_1 = int(de_1)
    de_2 = int(de_2)
    de_3 = int(de_3)
    point = Figure_and_points(de_1,de_2,de_3)
    return point

def Gagnant(score) :
    score = int(score)
    if score >= 343 :
        is_gagnant = True
    else :
        is_gagnant = False
    return is_gagnant
