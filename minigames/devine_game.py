import random 

def jouer_devine_nombre(joueurs):
    score = {}
    nbDeviner = random.randint(0,100)

    for joueur in joueurs:
        jdevine = input("Donne un nombre ! sois le plus proche !")
        nbj = int(jdevine)
        score[joueur] = abs(nbj - nbDeviner)