from players.player import Player
from game.card import Card
from game.nimmtGame import NimmtGame
from random import shuffle
from players.humanPlayer import HumanPlayer


class MedianCardBot(HumanPlayer):
    def __init__(self, name="roat"):
        super().__init__(name)
    
    def player_turn(self, game):
        # Filter available cards that can be played
        #valid_cards = [card for card in self.hand if card <= game.table[-1][-1]] (i can't do this operation (<=))
        valid_cards = [card for card in self.hand if self.compare_cards(card, game.table[-1][-1])]

        
        if not valid_cards:#(i have to review this function, when the bot choose the weakest card, he ends up picking all the line and that's not good )
            # If there is no safe card, choose the weakest card among all available cards
            return min(self.hand)
        
        # Sort available cards by increasing value
        valid_cards.sort()


        # Choose the card that is closest to the median of the available cards
        median_index = len(valid_cards) // 2
        #closest_to_median = min(valid_cards, key=lambda card: abs(card - valid_cards[median_index]))(I can't do the substuction without a function)
        closest_to_median = min(valid_cards, key=lambda card: abs(self.subtract_cards(card, valid_cards[median_index])))
        
        return closest_to_median
    
    def compare_cards(self, card1, card2):
        return card1.value <= card2.value
   

    def subtract_cards(self, card1, card2):
        return card1.value - card2.value
