from player import Joueur

board = ["normal", "bonus", "normal", "normal", "malus", "normal", "bonus", "normal", "normal", "malus"]
alice = Joueur("Alice")
bob = Joueur("Bob")
players = [alice, bob]
# print(f"voici le plateau de jeux : {plateau}") 

def afficher_plateau(plateau, joueurs):
    nP = len(plateau)
    nJ = len(joueurs)
    plat = ""

    for i in range(nP):
        joueurs_ici = []
        contenu = f"[{plateau[i]}]"
        for j in range(nJ):
            if joueurs[j].position == i:
                joueurs_ici.append(joueurs[j].nom)
        
        if joueurs_ici != []:
            contenu = f"[{"/".join(joueurs_ici)}]"
        else:
            contenu = f"[{plateau[i]}]"
        
        plat += contenu
            
            
    print(plat)

#afficher_plateau(board, players)