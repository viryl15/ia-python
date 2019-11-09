import nouveau as n
import conversation as conv
from random import randint

# DECLARATION DES FONCTIONS


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


# DEBUT

liste1 = []
i = 0


with open("ressources/conversations/conversationEnCour.txt", "a") as conversation:
    with open("ressources/conversations/debutSalutations.txt", "r") as salutation:
        for line in salutation:  # Enregistrement de la liste des salutation dans un tableau (list)
            i += 1
            line = line.strip()
            liste1.append(line)
        j = randint(0, liste1.__len__()) - 1
        print(liste1[j])
    conversation.write(liste1[j] + "\n")
    ans = input()
    ans = ans.strip()
    ans = ans.upper()
    if ans != "\n":
        if ans == "SALUT" or ans == "SALUT !" or ans == "BONJOUR" or ans == "BONSOIR":
            print("JE SUIS FIRSTIA ET TOI ?")
            conversation.write("JE SUIS FIRSTIA ET TOI ?\n")
            ans = input()
            ans = ans.strip()
            ans = ans.upper()
            if ans.endswith("?"):
                n.recherche(ans)
            # print("ENCHANTE ",(ans.upper()-"MOI C'EST "),"COMMENT TU VAS ?")
            print("COMMENT TU VAS ?")
            conversation.write("COMMENT TU VAS ?\n")
            ans = input()
            ans = ans.strip()
            ans = ans.upper()
            if ans == "JE VAIS BIEN ET TOI ?" or ans == "BIEN ET TOI ?":
                print("COOL")
                conversation.write("COOL\n")
                ans = input()
                ans = ans.strip()
                ans = ans.upper()
                if ans == "aimer cest quoi ?" or ans == "POURQUOI" or ans == "POURQUOI?":
                    print("JE SUIS UNE MACHINE")
                    conversation.write("JE SUIS UNE MACHINE\n")
                    createur()
                    conv.continuer()
                else:
                    createur()
                    n.recherche(ans)

            elif ans == "JE VAIS BIEN" or ans == "BIEN" or ans == "JE ME PORTE BIEN" or ans == "JE VAIS ASSEZ BIEN" or ans == "JE SUIS EN FORME":
                print("COOL !!!")
                conversation.write("COOL !!!\n")
                createur()
                conv.continuer()
                # continue()
            elif ans == "JE VAIS MAL" or ans == "TRES MAL" or ans == "JE NE VAIS PAS BIEN" or ans == "JE ME SENT MAL" or ans == "JE NE ME SENT PAS BIEN" or ans == "MAL":
                print("QU'EST-CE-QUI NE VA PAS ?")
                print("EST-TU SOUFRANT ? O/N")
                conversation.write("QU'EST-CE-QUI NE VA PAS ?\n")
                conversation.write("EST-TU SOUFRANT ? O/N\n")
                ans = input()
                ans = ans.strip()
                ans = ans.upper()
                if ans == "OUI" or ans == "O":
                    print("TU SOUFFRES DE QUOI ?")
                    conversation.write("TU SOUFFRES DE QUOI ?")
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
                # continue()
            else:
                n.recherche(ans)



        else:
            n.recherche(ans.upper())

# Nouvelle ligne 2
