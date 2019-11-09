##import pickle
##
##score1 = {"j1":4, "j2":56, "j3":30}
##
##with open("ressources/data", "wb") as data:
##    my_pickler = pickle.Pickler(data)
##    my_pickler.dump(score1)
##
##with open("ressources/data", "rb") as data:
##    my_depickler = pickle.Unpickler(data)
##    recup = my_depickler.load()
##print(recup)

from random import randint
from random import uniform
from compatible import testOfCompatibilitie as toc2
i=0
j=0
#liste1 = list()
liste1 = []

print(toc2("EN GÉOMÉTRIE, COMBIEN DE CÔTÉS POSSÈDE UN LOSANGE", "COMBIEN Y A-T-IL DE SIGNES DE FEU"))


try:
    with open( "ressources/conversations/debutSalutations.txt", "r" ) as salutation:
        #content = ressources1.read()
        #print(content.splitlines())
        for line in salutation:  # Enregistrement de la liste des questions dans un tableau (list)
            i += 1
            line = line.strip()
            #line = (line.strip()).replace("'", "_")
            liste1.append(line)
        print(liste1.__len__())
        chaine = "ma chaine SALUT "
        print(chaine.replace("a",""))
        j = randint(0,liste1.__len__())-1
        print(liste1[j])
except FileNotFoundError as e:
    print("Le fichier {} n'existe pas !".format(e.filename))
    exit(1)
except PermissionError as e:
    print("Droit de lecture absent sur le fichier {} !".format(e.filename))
    exit(2)
except Exception as e:
    print("Une erreur a empeche l'ouverture du fichier : ".format(e.filename))
with open( "ressources/test.txt", "a" ) as ressources1:
        ressources1.close()
