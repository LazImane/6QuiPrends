from players.player import Player 
from game.card import Card 

class TheStrong(Player):
    def __init__(self) -> None:
       
        self.name='The Strong'
        self.score=0
        self.hand=[]

    def info(self, message):
        
        print("@"+self.name+" : ",message)

    def getCardToPlay(self):
        if not self.hand: 
            return None
        return max(self.hand)

   
    
    def getLineToRemove(self, game):
       
         if not game.table:  # Vérifie si la table de jeu est vide
            return None
         return game.table.index(max(game.table)) 

    def player_turn(self, game):
        # Gère le tour de jeu du bot
        self.info(game.display_scores())
        self.info(game.display_table())

        if not self.hand:  # Vérifie si la main du bot est vide
            self.info("La main du bot est vide.")
            return None

        card_to_play = self.getCardToPlay()
        self.info(f"Le bot joue la carte : {card_to_play}")

        return card_to_play
