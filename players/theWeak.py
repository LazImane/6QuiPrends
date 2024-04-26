from players.player import Player
from game.card import Card

class TheWeak(Player):
     def __init__(self):
         self.name="The WEAK"
         self.score = 0
         self.hand = []

     def info(self, message):
        print(f"{self.name}: {message}")
   
     def getCardToPlay(self):
      #le bot choisi la carte la plus faible est return la carte 
      # la plus faible dansla main du bot
        
        if not self.hand:  # Vérifie si la main du bot est vide
            return None
        return min(self.hand)  # Choix de la carte la plus faible dans la main du bot
       
     def getLineToRemove(self, game):
      
        ligne = 1
        for i,row in enumerate(game.table):
            score = game.total_cows(row)
            if(score < game.total_cows(row)):
                ligne = i
        return ligne

     def player_turn(self, game):
      #gere le tour de jeu du bot
      
        self.info(game.display_scores())
        self.info(game.display_table())
        
        if not self.hand:  # Vérifie si la main du bot est vide
            self.info("La main du bot est vide.")
            return None

        card_to_play = self.getCardToPlay()
        self.info(f"Le bot joue la carte : {card_to_play}")

        return card_to_play
