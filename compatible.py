from math import *



def testOfCompatibilitie(chaine1,chaine2):
    chaine1 = chaine1.replace("?", " ")
    chaine2 = chaine2.replace("?", " ")
    a = (chaine1.strip()).replace("_", " ")
    b= (chaine2.strip()).replace("_", " ")
    c = min(len(a), len(b))
    
    if c != len(a):
        d=a
        a=b
        b=d

    aTab = list()
    bTab = list()
    aTab = a.split(" ")
    bTab = b.split(" ")
    #print(aTab)
    for k,mot in enumerate(aTab):
         continue
    percentage = 0
    i = 0
    
    for j in  range(k+1):
        if bTab.__contains__(aTab[j].strip()):
            i+=1

        percentage = i/(bTab.__len__())*100

    if percentage >= 30 and percentage <= 70:
        #print("Compatibilitie of level 1 with ", chaine2, percentage, "%")
        percentage = testOfCompatibilitie2(a,b)
        #print("level 2 ", percentage)
        if percentage >= 50:
            #print("Compatibilitie of level 2 with ", chaine2, percentage, "%")
            return 2,percentage
        else:
            #print("Non Compatibilitie with of level 2", chaine2, percentage, "%")
            return 2,percentage
        #return True
    elif percentage > 70:
        #print("Compatibilitie with ", chaine2, percentage, "%")
        return 1,percentage
    else:
        #print("Non Compatibilitie with of level 1", chaine2, percentage, "%")
        #print(chaine2)
        #return False

        return 1,percentage


##chaine1 = str(object = "   AS TU FAIM ????")
##print(type(chaine1))
##chaine2 = "TU AS FAIM ?     "   
##print(testOfCompatibilitie(chaine1,chaine2))

def testOfCompatibilitie2(chaine1,chaine2):
    chaine1 = chaine1.replace("?", " ")
    chaine2 = chaine2.replace("?", " ")
    a = (chaine1.strip()).replace("_", "'")
    b = (chaine2.strip()).replace("_", "'")
    c = min(len(a), len(b))
    d = len(a)
    e = len(b)

    if c != len(a):
        g = a
        a = b
        b = g
    #On coupe la chaine b pour quelle ai la meme taille que a
    #b = b[:len(a)]

    for k, mot in enumerate(a):
        continue

    percentage = 0
    i = 0
    l = 0
    p = 0
    q = 0
    ####resultats acceptable voir si l'amelioration est possible

    # for j in  range(len(a)):
    #     if b.__contains__(a[j].strip()): #verifie si la chaine la plus longue contient le caractere de rang j de la chaine courte
    #         g = b.count(a[j].strip())
    #         if g == 1:
    #             f = b.index(a[j])
    #             g = a.index(a[j])
    #             if (f <= g + 1) and (f >= g - 1):
    #                 i+=1
    #                 p = i/ len(a) * 100
    #         elif g <= a.count(a[j].strip()) + 1 and g >= a.count(a[j].strip()) - 1:#test si les chaines ont le meme nombre aproximatif de caractere g
    #         #elif g == a.count(a[j].strip()):
    #             i += 1
    #             p = i / len(a) * 100
    #     else:
    #         i -= 1
    #         p = i / len(a) * 100


    # for l in  range(len(a)):
    #     if b.__contains__(a[l].strip()): #verifie si la chaine la plus longue contient le caractere de rang l de la chaine courte
    #         g = b.count(a[l].strip())
    #         h = a.count(a[l].strip())
    #         b = a.replace(a[l].strip(), "")
    #         a = a.replace(a[l].strip(), "")
    #
    #         percentage += h/g
    #     else:
    #         percentage += 0

    ####efficace, doit etre ameliorer

    l = 0
    n = 0
    p = a
    q = b
    while l >= 0 and l < len(a) and len(a) != 0:
        #print("test")
        if b.__contains__(a[l].strip()): #verifie si la chaine la plus longue contient le caractere de rang l de la chaine courte
            g = b.count(a[l].strip())
            h = a.count(a[l].strip())
            # print("a[l].strip() ", a[l].strip())
            # print("g = ", g, "et h = ", h)
            b = b.replace(a[l].strip(), "")
            a = a.replace(a[l].strip(), "")
            a = a.strip()
            b = b.strip()
            # print("a = ",a)
            # print("b = ",b)
            percentage += h/g

            # if l == 0:
            #     l = 0
            # elif l > 0:
            #     l -= 1
        else:
            #l += 1
            n += 1
            a = a.replace(a[l].strip(), "")#supprimer la lettre qui n'est pas dans la chaine b
            a = a.strip()#suppression des espaces(vides) autour de la chaine a
        # if a == "":
        #     break
    ######## Essayer de combiner les deux si possible
        # print("b = ", b)
    return percentage*10-n/len(p)*100-len(b)/len(q)*100
