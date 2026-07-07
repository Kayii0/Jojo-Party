class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.position = 0
        self.pieces = 5


alice = Joueur("Alice")
print(alice.nom, alice.position, alice.pieces)