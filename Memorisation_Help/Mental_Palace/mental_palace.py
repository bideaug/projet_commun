#! /usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt
import os.path
import make_dir

user_path,path_to_dic = make_dir.Make_direction()
logname = os.environ['LOGNAME']

boucle = True
test = True 
i = 0 #variable de choix de la session 1 nouvelle 2 ancienne
#if logname == "aurigolys" :
#    path_to_dictionnaire = "/home/"+logname+"/Documents/programme/projet_commun/Memorisation_Help/Mental_Palace/dic.txt"
#else : 
#    path_to_dictionnaire = "/home/"+logname+"/projet_commun/Memorisation_Help/Mental_Palace/dic.txt"
fichier = open(path_to_dic,"r")
lecture = fichier.read()
lecture = lecture.lower()
word = lecture.split()


while boucle :
    try : 
        if os.path.isfile(user_path+"/log_1.txt") : 
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
    boucle = True
    k=0
    for j in os.listdir(user_path):
        if 'log_' in j:
            k+=1
    while boucle:
        try : 
            i = input(str(k)+" Palais mental. Entrez le numero de celui a tester:\n")
        except :
            print ("Mauvaise entree\n")
        if i<k or i>k : 
            print ("Mauvaise entree\n")
        else : boucle=False

    logfile = open(user_path+"/log_"+str(i)+".txt","r") 
    verifiaction = str()
    verification = raw_input("Veuillez entrer la liste de mot dans l'ordre\n")
    log = logfile.read()
    log = log.lower()
    print log

else :
    k=0
    for j in os.listdir(user_path):
        if 'log_' in j:
            k+=1

        logfile = open(user_path+"/log_"+str(k+1)+".txt","w")
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

