#! /usr/bin/python2.7

import time
import commands

continuer = True
def save():
    utilisateur=commands.getstatusoutput('ls ./utilisateurs')
    print("les utilisateurs sont : ",utilisateur)

while continuer == True :

    print("appuyez sur la touche enter :")
    depart = raw_input()
    t0=time.time()

    fin = raw_input()
    t1=time.time()
    print("Vous avez mis : ",t1-t0," s")

    print("Voulez vous sauvegarder votre score ? y/n")
    score = raw_input()
    if (score == "y" or score == "Y" ) :
        save_success=save()
    else :
        save = False
    

    print("Voulez vous rejouez ? y/n")
    choix=raw_input()
    if (choix == "y" or choix == "Y" ) :
        continuer = True
    else :
        continuer = False

