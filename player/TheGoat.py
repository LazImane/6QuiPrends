from players.player import Player
from game.card import Card
#from game.nimmtGame import NimmtGame  

class TheGOAT(Player):
    def __init__(self):
        self.name="The GOAAT"
        self.score = 0
        self.hand = []

    def info(self, message):
        #on affiche pas de messages
        pass

    def getLineToRemove(self, game):
        """
        obtenir la ligne avec un score minimum

        :param game: le jeu en cours
        :return: la ligne à enlever
        """
        score = 0
        ligne = 1
        for i,row in enumerate(game.table):
            if(score > game.total_cows(row)):
                ligne = i

        
    def getCardToPlay(self):    
        """
        Permet d'obtenir la carte à jouer.

        :return: La réponse du joueur.
        """    
        while True:
            try:
                response = int(input(f"@{self.name} ({self.score}🐮) quelle carte voulez-vous jouer ? "))
                if response <= 0:
                    raise ValueError
                return response
            except ValueError:
                self.info("Veuillez entrer un nombre entier positif.")
    
    def player_turn(self, game):
        """
        Gère le tour de jeu d'un joueur.

        :param game : le jeu en cours
        """
        self.info(game.display_scores())
        self.info(game.display_table())
        while True:
            self.info(f"Votre main : {' '.join(map(str, self.hand))}")
            try:
                carteChoisie = Card(self.getCardToPlay())
                if carteChoisie in self.hand:
                    return carteChoisie
                else:
                    self.info("Vous n'avez pas cette carte dans votre main")
            except ValueError:
                self.info("Veuillez entrer un nombre entier correspondant à une carte dans votre main.")
