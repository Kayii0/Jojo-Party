from player import Joueur
from board import afficher_plateau
from dice import lancer_de

board = ["normal", "bonus", "normal", "normal", "jeux", "normal", "bonus", "shop", "normal", "normal", "jeux", "FIN"]
josh = Joueur("Josh")
coco = Joueur("coco")
kiwi = Joueur("kiwi")
darsto = Joueur("darsto")
players = [josh, coco, kiwi, darsto]

size = len(players)
partie_en_cours = True

while partie_en_cours:

    for i in range(size):
        actuel = players[i]
        
        jouer = input(f"\nA ton tour {actuel.nom} ! Voulez-vous lancer le dé ? (ou 'stop' pour quitter) : ")
        
        if jouer.lower() == 'stop':
            partie_en_cours = False
            break  # Sort du 'for'

        afficher_plateau(board, players)
            
        score = lancer_de()
        print(f"Dé = {score} !")
        actuel.position += score
            
        # on verifie si le joueur est sur la dernniere case 
        if actuel.position >= len(board) - 1:
            actuel.position = len(board) - 1  
            print(f"\n🎉 Félicitations {actuel.nom}, tu as atteint la fin du plateau !")
            partie_en_cours = False
            break  #  fin de partie ça sort

        if board[actuel.position] == "jeux" :
            print("Case Jeux !")
                
        afficher_plateau(board, players)

print("\n--- Fin de la partie ---")
afficher_plateau(board, players)