#! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt
import os.path

boucle = True
test = True 
i = 0 #variable de choix de la session 1 nouvelle 2 ancienne
fichier = open("dic.txt","r")

lecture = fichier.read()
lecture = lecture.lower()
word = lecture.split()

#print word

while boucle :
    try : 
        if os.path.isfile("log.txt") : 
            i = input("1) Nouvelle session de test\n2) Ancienne session de test\n")
        else :
            i = 1
        boucle = False
    except :
        print ("Mauvaise entree\n")
    if i!=1 and i!=2 : 
        print ("Mauvaise entree\n")
        boucle = True

if i==2 :
    logfile = open("log.txt","r")
    verifiaction = str()
    verification = raw_input("Veuillez entrer la liste de mot dans l'ordre\n")
    log = logfile.read()
    log = log.lower()
    print log

else :
        logfile = open("log.txt","w")
        nb_spots = 0.
        while test:
            try:
                nb_spots = input("Veuillez entrer le nombre de spot dans votre palais\n")
                test = False
            except :
                print ("Mauvaise entree\n")

        spots = []

        for i in np.arange(nb_spots):
            spots.append(word[np.random.randint(len(word))])
        print "Liste de mot a retenir"
        print spots
        for i in np.arange(len(spots)):
            logfile.write(spots[i]+" ")

