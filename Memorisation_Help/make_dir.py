import os

def Make_direction():
    logname = os.environ['LOGNAME']
    verification = True

    if "projet_commun" in os.getcwd():
        while "projet_commun" in os.get_cwd():
            os.chdir("..")
        
        path = os.getcwd()+"/projet_commun/Users_Files"
    
        print "veuillez indiquer votre numero d'utilisateur:\n"
        if os.path.isdir(path):
            users = os.listdir(path)
            users.append("New user")
            print "Dossier d'utilisateurs existant"
        else :
            os.mkdir(path)
            users = ["New user"]
            print "Dossier d'utilisateurs cree"
    
        print users

        for i in users:
            print users.index(i),":",i,"\n"

        while verification:
            try :
                answer = input("numero :")
                print answer, users[answer]
                if users[answer] == 'New user':
                    dirname=raw_input("entrez le nom du nouvel utilisateur\n")
                    os.mkdir(path+"/"+dirname)
                    print("dossier cree")
                    os.chdir(path+"/"+dirname)
                    print("pwd ok")
                    verification = False
                else : 
                    os.chdir(path+"/"+users[answer])
                    verification = False
            except :
                verification = True
        user_path=path+"/"+users[answer]
    else:
        if os.path.isfile(direction.log):
          fichier = open("direction.log","r")
          path = fichier.read()
          path=path.lower

        else : 
            while verification:
                try:
                    path=raw_input("entrez un chemin valide pour la creaction de Users\n")
                    os.chdir(path)
                    verification = False
                except:
                    print "mauvaise entree"
            path = path+"/Users_Files"
            fichier = open("direction.log","w")
            fichier.write(path)
            os.mkdir(path)
        
        if os.path.isdir(path):
            users = os.listdir(path)
            users.append("New user")
            print "Dossier d'utilisateurs existant"
        else :
            os.mkdir(path)
            users = ["New user"]
            print "Dossier d'utilisateurs cree"
    
        print users

        for i in users:
            print users.index(i),":",i,"\n"

        while verification:
            try :
                answer = input("numero :")
                print answer, users[answer]
                if users[answer] == 'New user':
                    dirname=raw_input("entrez le nom du nouvel utilisateur\n")
                    os.mkdir(path+"/"+dirname)
                    print("dossier cree")
                    os.chdir(path+"/"+dirname)
                    print("pwd ok")
                    verification = False
                else : 
                    os.chdir(path+"/"+users[answer])
                    verification = False
            except :
                verification = True
        user_path=path+"/"+users[answer]
    return user_path 
