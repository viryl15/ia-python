from random import randint
import nouveau as n

import conversation as conv
import comprendPas as cp

#continuer une conversation
def continuer():
	liste1 = []
	liste2 = []
	conversationEnCour = []
	i = 0
	j = 0
	with open("ressources/conversations/conversationEnCour.txt", "r") as conversation:
		for line in conversation:
			conversationEnCour.append(line)
		conversation.close()
##    with open("ressources/conversations/conversationEnCour.txt", "w") as conversation:
##    	conversation.write("")
	with open("ressources/conversations/conversationEnCour.txt", "a") as conversation:
		try:
			with open( "ressources/questions/questionsList.txt", "r" ) as ressources1:
				for line in ressources1:
					#i+=1
					line = line[0:len(line)]
					liste1.append(line)

			with open( "ressources/questions/simpleExpressions.txt", "r" ) as ressources1:
				for line in ressources1:
					#i+=1
					line = line[0:len(line)]
					liste2.append(line)
				k = randint(0,3)
				if k == 0 or k == 1:
					j = randint(0,(len(liste1)-1))
					if liste1[j] not in conversationEnCour:
							if liste1[j].strip() == "" or liste1[j].strip() == "\n":
								continuer()
							c = liste1[j] + " ?"
							print( c.replace("\n", "") )
							conversation.write("\n"+liste1[j])
							ans = input()
							ans = ans.strip()
							ans = ans.upper()
							if ans.endswith("?") or ans.endswith("!"):
									n.recherche(ans)
							elif ans.lower() == "je ne sais pas" or ans.lower() == "sais pas" or ans.lower() == "j'sais pas" or ans.lower() == "j sais pas":
								liste3 = []
								#print("Fichier utilise: ", (liste1[j]).strip().replace("'","_"))
								with open( "ressources/questions/"+(liste1[j]).strip().replace("'","_")+".txt", "r" ) as ressources1:
									for line in ressources1:
										line = line[0:len(line)]
										liste3.append(line)
								if len(liste3)>1:
									l = randint(0,(len(liste3)-1))
									print("reponse: ", liste3[l])
								else:
									print("reponse: ", liste3[0])
								continuer()
							else:

								#cp.ajout((liste1[j][:len(liste1[j])]), ans)
								continuer()
								#n.recherche(ans)
					else:
						continuer()
				else:
					j = randint(0,(len(liste2)-1))
					if liste2[j] not in conversationEnCour:

						c = (liste2[j]).replace("\n", "").strip()#(liste2[j][:len(liste2[j])]) print( c )
						conversation.write("\n"+liste2[j]) 
						ans = input() 
						ans = ans.strip() 
						ans = ans.upper() 
						if ans.endswith("?"):
							n.recherche(ans)

						else:
							cp.ajoutSimple(ans)
							continuer()
							#n.recherche(ans)
					else:
						continuer()
		except FileNotFoundError as e:
			print("Le fichier {} n'existe pas !".format(e.filename))
			exit(1)
		except PermissionError as e:
			print("Droit de lecture absent sur le fichier {} !".format(e.filename))
			exit(2)
		except Exception as e:
			print("Une erreur a empeche l'ouverture du fichier : {} ".format(e.filename))
			exit(3)
