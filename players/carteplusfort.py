from players.player import Player 
from game.card import Card 

class CartePlusForte(Player):
    def __init__(self) -> None:
        """
        Crée un joueur avec un nom donné.

        :param name: Le nom du joueur.
        """
        self.name='BOT@PLUSFORT'
        self.score=0
        self.hand=[]

    def info(self, message):
        """
        Affiche un message à l'attention du joueur.
        
        :param message: Le message à afficher.
        """
        print("@"+self.name+" : ",message)

    def getCardToPlay(self):
        """
        Permet d'obtenir la carte à jouer.

        :return: La réponse du bot.
        """
        while True:
                maxcarte = self.hand[0]
                for index , item in enumerate(self.hand):
                    if maxcarte.cowsNb < self.hand[index].cowsNb :
                        maxcarte = self.hand[index]
                return maxcarte.value
    
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
    
    def getLineToRemove(self, game):
        """
        permet d'obtenir la ligne à enlever quand la carte jouée était plus petite

        :param game: le jeu en cours
        :return: la ligne à enlever
        """
        print(game.table)
        for i,row in enumerate(game.table):
            score = game.total_cows(row)
            if(score <= game.total_cows(row)):
                ligne = i
                print(ligne)
        return ligne 

