#! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt
import os.path
import os
import cul_de_chouette_function as fct
import cul_de_chouette_objet as obj

Jouer = True
Nouvelle_partie = True
Premiere_partie = True
Gagnant = False
while Jouer == True :
    if Nouvelle_partie == True and Premiere_partie == True:
        nombre_de_joueur = input("entrer le nombre de joueur s'il vous plait (max 4): \n")
        nombre_de_joueur_a_creer=nombre_de_joueur
        while nombre_de_joueur_a_creer > 0 :
            joueur_numero = nombre_de_joueur-nombre_de_joueur_a_creer +1
            if joueur_numero == 1:
                nom_joueur_1 = raw_input('rentrer votre nom joueur 1 : ')
                score_joueur_1 = 0
            elif joueur_numero == 2:
                nom_joueur_2 = raw_input('rentrer votre nom joueur 2 : ')
                score_joueur_2 = 0
            elif joueur_numero == 3:
                nom_joueur_3 = raw_input("rentrer votre nom joueur 3 : ")
                score_joueur_3 = 0
            elif joueur_numero == 4:
                nom_joueur_4 = raw_input("rentrer votre nom joueur 4 : ")
                score_joueur_4 = 0
            else :
                print("Pas plus de 4 joueurs !!")
            nombre_de_joueur_a_creer = nombre_de_joueur_a_creer -1 

    Premiere_partie = False
    is_gagnant = False
        
    nb_etape = nombre_de_joueur
    joueur_actuelle = 1
    while nb_etape > 0 :
        nombre_de_joueur_a_afficher = nombre_de_joueur
#affiche les scores des joueurs au debut de leur tour
        while nombre_de_joueur_a_afficher > 0 :
                joueur_numero = nombre_de_joueur-nombre_de_joueur_a_afficher +1
                if joueur_numero == 1:
                    print("Les scores sont ",nom_joueur_1," : ",score_joueur_1,"\n")
                elif joueur_numero == 2:
                    print("Les scores sont ",nom_joueur_2," : ",score_joueur_2,"\n")
                elif joueur_numero == 3:
                    print("Les scores sont ",nom_joueur_3," : ",score_joueur_3,"\n")
                elif joueur_numero == 4:
                    print("Les scores sont ",nom_joueur_4," : ",score_joueur_4,"\n")
                else :
                    print("erreur ! ")
                    exit()
                nombre_de_joueur_a_afficher = nombre_de_joueur_a_afficher -1 
                
        if joueur_actuelle == 1 :
            nom = nom_joueur_1
            print("C'est au tour de",nom," de jouer ! ")
            point = fct.Tour_de_jeu()
            score_joueur_1 = score_joueur_1 + point
            is_gagnant = fct.Gagnant(score_joueur_1)
            if is_gagnant :
                print("Le joueur ",nom_joueur_1," a gagner avec :", score_joueur_1)
        
        elif joueur_actuelle == 2 :
            nom = nom_joueur_2
            print("C'est au tour de",nom," de jouer ! ")
            point = fct.Tour_de_jeu()
            if nombre_de_joueur == 2 :
                Actualisation_des_scores(score_joueur_1, score_joueur_2,point,modif_score_de)
            elif nombre_de_joueur == 3 :
                Actualisation_des_scores(score_joueur_1, score_joueur_2,score_joueur_3,point,modif_score_de)
            elif nombre_de_joueur == 4 :
                Actualisation_des_scores(score_joueur_1, score_joueur_2,score_joueur_3,score_joueur_4,point,modif_score_de)

            score_joueur_2 = score_joueur_2 + point
            is_gagnant = fct.Gagnant(score_joueur_2)
            if is_gagnant :
                print("Le joueur ",nom_joueur_2," a gagner avec :", score_joueur_2)
        
        elif joueur_actuelle == 3 :
            nom = nom_joueur_3
            print("C'est au tour de",nom," de jouer ! ")
            point = fct.Tour_de_jeu()
            score_joueur_3 = score_joueur_3 + point
            is_gagnant = fct.Gagnant(score_joueur_3)
            if is_gagnant :
                print("Le joueur ",nom_joueur_3," a gagner avec :", score_joueur_3)
            
        elif joueur_actuelle == 4 :
            nom = nom_joueur_4
            print('C\' est au tour de',nom,' de jouer !')
            point = fct.Tour_de_jeu()
            score_joueur_4 = score_joueur_4 + point
            is_gagnant = fct.Gagnant(score_joueur_4)
            if is_gagnant :
                print("Le joueur ",nom_joueur_4," a gagner avec :", score_joueur_4)
                
        joueur_actuelle=joueur_actuelle+1
        print(joueur_actuelle)
        nb_etape = nb_etape-1
        print(nb_etape)
        print(is_gagnant)
    
    #verifiation s il y a un gagnant
