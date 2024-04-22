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
        i =  random.randint(0,len(self.hand))
        return self.hand[i]



    
    def player_turn(self, game):
        """
        Gère le tour de jeu d'un joueur.
        :param game : le jeu en cours
        """
        while True:
            try:
                carteChoisie = Card(self.getCardToPlay())
                if carteChoisie in self.hand:
                    return carteChoisie
            except ValueError:
                self.info("Veuillez entrer un nombre entier correspondant à une carte dans votre main.")
