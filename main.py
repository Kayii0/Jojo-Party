from player import Joueur
from board import afficher_plateau
from dice import lancer_de

board = ["normal", "bonus", "normal", "normal", "malus", "normal", "bonus", "normal", "normal", "malus"]
josh = Joueur("Josh")
players = [josh]

josh.position = 8
afficher_plateau(board, players)
jouer = input("Voulez-vous lancez le dé ?")

if jouer != "":
    score = lancer_de()
    print(f"dé = {score} !")
    players[0].position += score
    if players[0].position > len(board) - 1:
        players[0].position = len(board) - 1

afficher_plateau(board, players)