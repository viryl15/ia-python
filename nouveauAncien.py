import comprendPas as cp
import conversation as conv

def recherche(ans):
    i=0
    j=0
    liste1 = []
    if ans.endswith("?"):
        try:
            with open( "ressources/questions/questionsList.txt", "r" ) as questions:
                for line in ressources1:
                    i+=1
                    line = line[0:len(line)-1]
                    liste1.append(line)
                    
                #print(liste1)
            with open( "ressources/ressources1.txt", "r" ) as ressources1:
                for line in ressources1:
                    if ans in liste1:
                        j=liste1.index(ans)
                        if ans.endswith("?"):
                           print(liste1[j+1])
                           conv.continuer()
                           break
                        else:
                            print(liste1[j-1])
                            conv.continuer()
                            break
                    else:
                        cp.comprendPas(ans)
                        break
                    
        except FileNotFoundError as e:
                print("Le fichier {} n'existe pas !".format(e.filename))
                exit(1)
        except PermissionError as e:
                print("Droit de lecture absent sur le fichier {} !".format(e.filename))
                exit(2)
        except Exception as e:
                print("Une erreur a empeche l'ouverture du fichier : ".format(e.filename))
                exit(3)

