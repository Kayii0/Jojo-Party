from player import Joueur
from board import afficher_plateau
from dice import lancer_de

board = ["normal", "bonus", "normal", "normal", "malus", "normal", "bonus", "shop", "normal", "normal", "malus"]
josh = Joueur("Josh")
players = [josh]

josh.position = 0
jouer = input("Voulez-vous lancer le dé ? (ou tapez 'stop' pour quitter) : ")

while jouer != "stop" and josh.position < len(board) - 1:
    afficher_plateau(board, players)
    
    score = lancer_de()
    print(f"\nDé = {score} !")
    josh.position += score
    
    if josh.position >= len(board) - 1:
        josh.position = len(board) - 1
        print("Félicitations, vous avez atteint la fin du plateau !")
        break # A RETENIR ( break sert a sortir de la boucle )
        
    afficher_plateau(board, players)
    jouer = input("Voulez-vous rejouer ? (ou tapez 'stop') : ")

print("\n--- Fin de la partie ---")
afficher_plateau(board, players)