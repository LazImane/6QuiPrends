from players.player import Player
from game.card import Card
import random

class Random(Player):
    def __init__(self):
        self.name="Random"
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
        score = game.total_cows(game.table[0])
        for i,row in enumerate(game.table):
            #print("lihne :",i," score ",score)
            if(score >= game.total_cows(row)):
                score = game.total_cows(row)
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
           
