import nouveau as n
import conversation as conv

#DECLARATION DES FONCTIONS


def createur():
    print("VEUX TU SAVOIR QUI M'A CREE ? O/N")
    ans = input()
    ans = ans.strip()
    ans = ans.upper()
    if ans == "OUI" or ans == "O":
        print("MON CREATEUR S'APPELLE 'DYLAN TEMATIO'")

    else:
        print("DOMAGE !!!")
        conv.continuer()




#DEBUT

with open("ressources/conversations/conversationEnCour.txt", "w") as conversation:
    conversation.write("")
with open("ressources/conversations/conversationEnCour.txt", "a") as conversation:

    begin = "SALUT !!"
    print(begin)
    #conversation.write(begin+"\n")
    ans = input()
    ans = ans.strip()
    ans = ans.upper()
    if ans != "\n":
        if ans == "SALUT" or ans == "SALUT !" or ans == "BONJOUR" or ans == "BONSOIR":
            print("JE SUIS FIRSTIA ET TOI ?")
            #conversation.write(ans+"\n")
            #conversation.write("JE SUIS FIRSTIA ET TOI ?\n")
            ans = input()
            ans = ans.strip()
            ans = ans.upper()
            if ans.endswith("?"):
                n.recherche(ans)
            #print("ENCHANTE ",(ans.upper()-"MOI C'EST "),"COMMENT TU VAS ?")
            print("COMMENT TU VAS ?")
            ans = input()
            ans = ans.strip()
            ans = ans.upper()
            if ans == "JE VAIS BIEN ET TOI ?" or ans =="BIEN ET TOI ?":
                print("cool")
                ans = input()
                ans = ans.strip()
                ans = ans.upper()
                if ans == "aimer cest quoi ?" or ans == "POURQUOI" or ans == "POURQUOI?":
                    print("JE SUIS UNE MACHINE")
                    createur()
                    conv.continuer()
                else:
                    createur()
                    n.recherche(ans)

            elif ans == "JE VAIS BIEN" or ans =="BIEN" or ans == "JE ME PORTE BIEN" or ans == "JE VAIS ASSEZ BIEN" or ans == "JE SUIS EN FORME":
                print("COOL !!!")
                createur()
                conv.continuer()
                #continue()
            elif ans == "JE VAIS MAL" or ans == "TRES MAL" or ans == "JE NE VAIS PAS BIEN" or ans == "JE ME SENT MAL" or ans == "JE NE ME SENT PAS BIEN" or ans == "MAL":
                print("QU'EST-CE-QUI NE VA PAS ?")
                print("EST-TU SOUFRANT ? O/N")
                ans = input()
                ans = ans.strip()
                ans = ans.upper()
                if ans == "OUI" or ans == "O":
                    print("TU SOUFFRES DE QUOI ?")
                    ans = input()
                    ans = ans.strip()
                    print("JE SUIS NAVRE")
                    createur()
                    conv.continuer()
                elif ans == "NON" or ans == "N":
                    print("QU'EST-CE-QUI NE VA PAS ?")
                    ans = input()
                    ans = ans.strip()
                    print("JE SUIS NAVRE")
                    createur()
                    conv.continuer()
                #continue()
            else:
                n.recherche(ans)



        else:
            n.recherche(ans.upper())

