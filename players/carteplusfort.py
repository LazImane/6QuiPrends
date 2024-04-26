from players.player import Player 
from game.card import Card 

class TheStrong(Player):
    def __init__(self) -> None:
        self.name='The Strong'
        self.score=0
        self.hand=[]

    def info(self):
        pass

    def carteMax(self):
        carteMax = self.hand[0]
        for card in self.hand :
            if card.value >= carteMax.value :
                carteMax = card
        return carteMax

    def getCardToPlay(self):
        if not self.hand: 
            return None
        return self.carteMax()

   
    
    def getLineToRemove(self, game):
        score = game.total_cows(game.table[0])
        for i,row in enumerate(game.table):
            #print("lihne :",i," score ",score)
            if(score >= game.total_cows(row)):
                score = game.total_cows(row)
                ligne = i
        return ligne

    def player_turn(self, game):

        if not self.hand:  # Vérifie si la main du bot est vide
            #self.info("La main du bot est vide.")
            return None

        card_to_play = self.getCardToPlay()
        #self.info(f"Le bot joue la carte : {card_to_play}")

        return card_to_play
