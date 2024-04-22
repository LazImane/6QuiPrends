from players.player import Player
from game.card import Card
import random

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
        ligne = 1
        for i,row in enumerate(game.table):
            score = game.total_cows(row)
            if(score < game.total_cows(row)):
                ligne = i
        return ligne

        
    def getCardToPlay(self):    
        """
        Choisie aléatoirement une carte.

        :return: une carte aléatoire selon un index random entre 0 et la taille du tableau hand
        """ 
        i =  random.randint(0,len(self.hand))-1
        print('the hand of the bot',self.hand)
        print('the random index',i)
        return self.hand[i].value
 
    def player_turn(self,game):
        """
        Gère le tour de jeu d'un joueur.
        :param game : le jeu en cours
        """
        carteChoisie = Card(self.getCardToPlay())
        return carteChoisie
           
