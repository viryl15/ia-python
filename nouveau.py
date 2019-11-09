#import comprendPas as cp
from comprendPas import *
import conversation as conv
from random import randint
from compatible import testOfCompatibilitie as toc

def recherche(ans):
    """

    :rtype:
    """
    i=0
    j=0
    
    liste1 = []
    liste2 = []
    liste3 = []
    if ans.endswith("?"):
        ans1 = ans
        while ans.endswith("?"):
            ans = ans[:len(ans)-1].strip()
        try:
            with open( "ressources/questions/questionsList.txt", "r" ) as questions:
                for line in questions: #Enregistrement de la liste des questions dans un tableau (list)
                    i+=1
                    line = line.strip()
                    line = line[:len(line)]
                    line = (line.strip()).replace("'", "_")
                    liste1.append(line)
            percentage1 = 0
            percentage2 = 0
            percentage = 0
            q = 0
            p = 0
            a1 = 0
            a2 = 0
            l = 0
            for s, t in enumerate(liste1): #Recuperation des pourcentages de reponses avec niveau de compatibilite
                l,p = toc((ans[:len(ans)]).strip().replace("'", "_"), t)
                #print("level: ", l, "percentage: ", p)
                if percentage1 < p and l == 1:
                    percentage1 = p
                    a1 = s
                elif percentage2 < p and l == 2:
                    percentage2 = p
                    a2 = s
                else:
                    q = p
                    a = s
            #prise de la reponse avec prioritee de niveau 1
            if percentage1 >= 75:
                percentage = percentage1
                a = a1
            elif percentage2 >= 75:
                percentage = percentage2
                a = a2
            else:
                percentage = q

            if ((ans).strip()) in liste1: #verifie si la question est connue
                with open( "ressources/questions/" + (ans).replace("'", "_") + ".txt", "r" ) as questions: #ouverture du fichier contennant les reponses a la question posee
                    #print("in list")
                    for elt in questions:
                        i+=1
                        elt = elt[:len(elt)]
                        liste2.append(elt)
                    #print(len(liste2))
                    if len(liste3) > 0:
                        j = randint(0,len(liste2)-1)#choix d'une reponse aleatoire
                        print(liste2[j])
                        conv.continuer()
                    else:
                        print(liste2[0])
                        conv.continuer()
            elif percentage >= 75 and liste1.__sizeof__() != 0 : #si la compatibilite est bonne
                #print("test1")
                with open( "ressources/questions/" + liste1[a] + ".txt", "r" ) as questions: #ouverture du fichier contennant les reponses 'possible' a la question posee
                    for elt in questions:
                        elt = elt[:len(elt)]
                        liste3.append(elt)
                    if len(liste3) > 0:
                        j = randint(0,len(liste3)-1)#choix d'une reponse aleatoire
                        print(liste3[j])
                        conv.continuer()
                    else:
                        print(liste3[0])
                        conv.continuer()
            #######Implementer cette partie dans comprend pas et l'effacer ici
            else:
                comprendPas(ans1.strip().upper())
                #for k, line in enumerate(liste1):
                    #if liste1.__contents__((ans[:len(a)-1]).strip()):
                    #if (ans[:len(a)-1]).strip() == line: #verifie si la question est dans la liste des questions connues
                        
                           #break
                    
                    
        except FileNotFoundError as e:
                print("Le fichier {} n'existe pas !".format(e.filename))
                exit(1)
        except PermissionError as e:
                print("Droit de lecture absent sur le fichier {} !".format(e.filename))
                exit(2)
        except Exception as e:
                print("Une erreur a empeche l'ouverture du fichier : ".format(e.filename))
                exit(3)
    else:#ajout dans les expressions simples
        with open( "ressources/questions/simpleExpressions.txt", "r" ) as expressions:
        	for line in expressions: #Enregistrement de la liste des expressions simples dans un tableau (list)
        		i+=1
        		line = line[:len(line)-1]
        		line = (line.strip())#.replace("'", "_")
        		liste1.append(line)
        		#print(liste1)
        if (ans.upper().strip()) in liste1: #Verifie si l'expression est connue
        	with open( "ressources/questions/simpleExpressions.txt", "r" ) as expressions: #ouverture du fichier contennant les expressions simples
        		for elt in expressions:
        			elt = elt[:len(elt)]
        			liste2.append(elt)
        		j = randint(0,len(liste2)-1)#choix d'une reponse aleatoire
        		print(liste2[j])
        		conv.continuer()
        else:
        	comprendPas(ans.upper().strip())
