#! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt
import os.path
import os
import cul_de_chouette_function as fct
import cul_de_chouette_objet as obj

"""
Je ne sais pas pourquoi je ne peux pas faire passer des Booleen en argument pour la methode de Chouette_velute

Et rajouter les autres regles et ensuite faire un truc qui permet de les prendre en compte ou pas genre 
Par defaut on active tout et
rentrer les regles que vous ne voulez pas
a = :_
False regle de a
et apres quand on regarde si sa fait un truc ou pas on instantie que les trucs true.
"""
Jouer = True
Nouvelle_partie = True
Premiere_partie = True
while Jouer == True :
    if Nouvelle_partie == True and Premiere_partie == True:
        nombre_de_joueur = input("entrer le nombre de joueur s'il vous plait (max 4): \n")
        nombre_de_joueur_a_creer=nombre_de_joueur
        while nombre_de_joueur_a_creer > 0 :
            joueur_numero = nombre_de_joueur-nombre_de_joueur_a_creer +1
            if joueur_numero == 1:
                nom = raw_input('rentrer votre nom joueur 1 : ')
                joueur_1 = obj.Joueur(nom,0)
            elif joueur_numero == 2:
                nom = raw_input('rentrer votre nom joueur 2 : ')
                joueur_2 = obj.Joueur(nom,0)
            elif joueur_numero == 3:
                nom = raw_input("rentrer votre nom joueur 3 : ")
                joueur_3 = obj.Joueur(nom,0)
            elif joueur_numero == 4:
                nom = raw_input("rentrer votre nom joueur 4 : ")
                joueur_4 = obj.Joueur(nom,0)
            else :
                print("Pas plus de 4 joueurs !!")
            nombre_de_joueur_a_creer = nombre_de_joueur_a_creer -1 
        Premiere_partie = False
    nb_etape = nombre_de_joueur
    joueur_actuelle = 1
    while nb_etape > 0 :
        if joueur_actuelle == 1 :
            nom = obj.Joueur.__affichage__(joueur_1)
            print("C'est au tour de",nom," de jouer ! ")
            fct.Tour_de_jeu(joueur_1)
        elif joueur_actuelle == 2 :
            nom = obj.Joueur.__affichage__(joueur_2)
            print("C'est au tour de",nom," de jouer ! ")
            fct.Tour_de_jeu(joueur_2)
        elif joueur_actuelle == 3 :
            nom = obj.Joueur.__affichage__(joueur_3)
            print("C'est au tour de",nom," de jouer ! ")
            fct.Tour_de_jeu(joueur_3)
        elif joueur_actuelle == 4 :
            nom = obj.Joueur.__affichage__(joueur_4)
            print("C'est au tour de",nom," de jouer ! ")
            fct.Tour_de_jeu(joueur_4)
        joueur_acutelle=joueur_actuelle+1
        nb_etape = nb_etape-1
"""
    elif Nouvelle_partie == True and Premier_partie == False :
        choix = raw_input("Voulez vous garder les memes joueurs ? Oui ou Non \n")
        if choix == O or choix == o:
            print("Vous garder les meme joueurs, bonne partie ;)")
#remettre les scores a zero
        else :
#y faudrai surement detruire les objets joueur de la partie d'avant
            nombre_de_joueur = fct.Creation_partie()
"""
#verifiation s il y a un gagnant

