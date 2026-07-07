board = ["normal", "bonus", "normal", "normal", "malus", "normal", "bonus", "normal", "normal", "malus"]

# print(f"voici le plateau de jeux : {plateau}") 

def afficher_plateau(plateau):
    n = len(plateau)
    plat = ""

    for i in range(n):
        plat += f"[{plateau[i]}]"
    
    print(plat)

afficher_plateau(board)