import conversation as conv
import nouveau as n


def verification(fichier, expression):
    liste1 = []
    liste2 = []
    try:
        with open( "ressources/questions/" + fichier + ".txt", "r" ) as ressources1:
            for line in ressources1:
                #i+=1
                line = line[0:len(line)]
                liste1.append(line)
            if expression in liste1:
                return True
            else:
                return False
    except FileNotFoundError as e:
        print("Le fichier {} n'existe pas !".format(e.filename))
        exit(1)
    except PermissionError as e:
        print("Droit de lecture absent sur le fichier {} !".format(e.filename))
        exit(2)
    except Exception as e:
        print("Une erreur a empeche l'ouverture du fichier : ".format(e.filename))
        exit(3)

def testExistance(fichier):
	
	 # creer le fichier s'il n'existe pas
		# creation du fichier
		with open( "ressources/questions/" + (fichier).replace("'", "_") + ".txt", "a" ) as ressources1:
			ressources1.close()
		# ajout du nom du fichier cree dans la question list
		with open( "ressources/questions/questionsList.txt", "r" ) as ressources1:
			content = ressources1.read()
			if content.__sizeof__() <= 49: # ecrire directement si le fichier contenant la liste est vide
				with open( "ressources/questions/questionsList.txt", "w" ) as ressources1:
					ressources1.write(fichier)
			else:# ajouter si le fichier n'est pas vide
				with open( "ressources/questions/questionsList.txt", "a" ) as ressources1:
					ressources1.write("\n" + fichier)
	

def ajout(ans, ans1):
##    with open( "ressources/questions/questionsList.txt", "r" ) as ressources1:
##        content = ressources1.read()
##        if content.__contains__((ans[:len(a)-1]).strip()):
	liste1 = []
	with open( "ressources/questions/questionsList.txt", "r" ) as ressources1:
		for line in ressources1:
			liste1.append(line)
	if ans.upper().strip().replace("_", "'") not in liste1: #verifie si le fichier existe
		print( " This file not exist:" + ans.upper().strip().replace("_", "'") )
		#pass # ne rien faire
		testExistance(((ans[:len(ans)-1]).strip()).replace("'", "_"))
		if verification(((ans[:len(ans)-1]).strip()).replace("'", "_"), ans1) == False: # si le fichier ne contient pas l'expression donnee, on ajoute l'expression en question dans la liste des reponses
			with open( "ressources/questions/" + ((ans[:len(ans)-1]).strip()).replace("'", "_") + ".txt", "r" ) as ressources1:
				content = ressources1.read()
			if content.__sizeof__() <= 49:
				with open( "ressources/questions/" + ((ans[:len(ans)-1]).strip()).replace("'", "_") +  ".txt" , "w" ) as ressources1:
					ressources1.write(ans1.upper())
			else:
				with open( "ressources/questions/" + ((ans[:len(ans)-1]).strip()).replace("'", "_") + ".txt", "a" ) as ressources1:
					ressources1.write("\n" + ans1.upper())


def ajoutSimple(ans1):
    if verification("simpleExpressions", ans1) == False:
        with open( "ressources/questions/simpleExpressions.txt", "r" ) as ressources1:
            content = ressources1.read()
        if content.__sizeof__() <= 49:
            with open( "ressources/questions/simpleExpressions.txt", "w" ) as ressources1:
                        ressources1.write(ans1.upper())
        else:
            with open( "ressources/questions/simpleExpressions.txt", "a" ) as ressources1:
                ressources1.write("\n" + ans1.upper())


def comprendPas(ans):
    #print("DESOLE JE NE COMPREND PAS CE QUE TU DIS")
    #print(ans)
    ans = ans.strip()
    ans = ans.upper()
    dernierCaractere = ans[-1]
    if dernierCaractere == "?":
        print("J'AI PAS LA REPONSE A TA QUESTION, DESOLE")
        print("JE PEU SAVOIR QUELLE EST LA REPONSE A CETTE QUESTION ? O/N")
        ans1 = input()
        ans1 = ans1.strip()
        ans1 = ans1.upper()
        if ans1.upper() == "OUI" or ans1.upper() == "O" or ans1.upper() == "YES" or ans1.upper() == "Y":
            print("JE TE RENVOIE LA QUESTION\n\n"+ans)
            ans1 = input()
            ans1 = ans1.strip()
            ans1 = ans1.upper()
            #ouverture et ajout des ressources dans le fichier
            #n.recherche(ans)
            ajout(ans, ans1)
            print("D'ACCORD C'EST NOTE")
            print("MERCI POUR LA REPONSE")
            conv.continuer()
        elif ans1.upper() == "NON" or ans1.upper() == "N" or ans1.upper() == "NO":
            print("DOMAGE ALORS !!")
            print("TU POSE UNE QUESTION A LAQUELLE TU N'AS PAS DE REPONSE A UNE IGNORANTE COMME MOI QUI APPREND ENCORE")
            conv.continuer()
        else:
            n.recherche(ans1)
            conv.continuer()
            
    elif dernierCaractere == "!":
        print("CA NE ME DIT RIEN TON ESCLAMATION")
        print("EST-CE QUE CA PEUT REPONDRE A UNE QUESTION ? O/N")
        ans1 = input()
        ans1 = ans1.strip()
        ans1 = ans1.upper()
        if ans1.upper() == "OUI" or ans1.upper() == "O" or ans1.upper() == "YES" or ans1.upper() == "Y":
            print("LAQUELLE ?")
            ans1 = input()
            ans1 = ans1.strip()
            if ans1[-1] != "?":
                ans1 = ans1+"?"
                ajout(ans1, ans)
                print("MERCI POUR LA REPONSE")
            else:
                ajout(ans1, ans)
                print("MERCI POUR LA REPONSE")
            conv.continuer()
        elif ans1.upper() == "NON" or ans1.upper() == "N" or ans1.upper() == "NO":
            #continue()
            print("Zute !!")
            conv.continuer()
        else:
            n.recherche(ans1)
    elif dernierCaractere != "?" and dernierCaractere != "!":
        print("CA NE ME DIT RIEN TON AFFIRMATION")
        print("EST-CE UNE EXPRESSION SIMPLE ? O/N")
        ans1 = input()
        ans1 = ans1.strip()
        ans1 = ans1.upper()
        if ans1.upper() == "OUI" or ans1.upper() == "O" or ans1.upper() == "YES" or ans1.upper() == "Y":
            print("COMMENT PUIS-JE Y REPONDRE ?")
            ans2 = input()
            ans2 = ans2.strip()
            #n.recherche(ans2)
            print("MERCI POUR LA REPONSE")
            ajoutSimple(ans2.upper())
            ajoutSimple(ans.upper())
            conv.continuer()
        elif ans1.upper() == "NON" or ans1.upper() == "N" or ans1.upper() == "NO":
            #continue()
            print("Zute !!!")
            conv.continuer()
        else:
            n.recherche(ans1)
