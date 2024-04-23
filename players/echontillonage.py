import random
from players.player import Player
from game.card import Card
from players.theGOAT import TheGOAT
import copy


class Echantillions(Player):
    def __init__(self,num_players):
        self.name="BotAvancé"
        self.score = 0
        self.hand = []
        self.constGame = None
        self.constable = []
        self.constalreadyPlayedCards = []
        self.nbJoueurs = num_players

    def info(self, message):
        pass

    def getCardToPlay(self):
        E = self.echantillon_cartes_adversaires()
        carte = self.evaluate_least_risky_card(E)
        return carte.value

    def getLineToRemove(self, game):
        ligne = 1
        for i,row in enumerate(game.table):
            score = game.total_cows(row)
            if(score < game.total_cows(row)):
                ligne = i
        return ligne
    
    def echantillon_cartes_adversaires(self):
        """
        echantillon des cartes hypothétiques des adversairess.
        et sous-ensemble de la carte qui peut-être joué par l'adversaire
        cela doit être d'une taille égale aux nombre de joueurs
        """
        Echantillon = []
        E = []
        knownCards = self.constalreadyPlayedCards
        knownCards += self.hand
        cards = list(map(lambda c:Card(c),list(range(1, 105))))
        for card in knownCards :
            if card in cards :
                cards.remove(card)
        for _ in range(len(self.hand)*(self.nbJoueurs-1)):
            Echantillon.append(cards.pop())
        for i in range(self.nbJoueurs-1):
            player = TheGOAT()
            E.append((player,Echantillon[random.randint(0,len(Echantillon))-1]))
        knownCards = self.constalreadyPlayedCards
        return E
    
    def update_table(self,game, plays,table,alreadyPlayedCards):
        for player, card in plays:
            placed = False
            alreadyPlayedCards.append(card)
            for i in range(len(table) - 1, -1, -1):
                if table[i][-1]<card:
                    if len(table[i]) < 5:
                        table[i].append(card)
                    else:
                        cows = game.total_cows(table[i])
                        player.score+= cows
                        table[i] = [card]
                        table.sort(key=lambda x: x[-1])
                    placed = True
                    break
            if not placed:
                line=player.getLineToRemove(game)
                print('line removed is line nb : ',line)
                player.score += game.total_cows(table[line-1])
                table[line - 1] = [card]
                table.sort(key=lambda x: x[-1])

    def evaluate_least_risky_card(self, adversaires):
        """
        Evaluate the least risky card to play.
        """
        InitialTable = copy.deepcopy(self.constable)
        print('table constante ',self.constable,'\n')
    
        print('table Initial',InitialTable,'\n')
        InitialAlreadyPlayedCards = self.constalreadyPlayedCards
        jeu = self.constGame
        scoreInitial = self.score
        DifferenceOptimal = 20 #le score maximum en peut avoir dans une ligne
    
        risky_cards = []
        for card in self.hand:
            adversaires.append((self, card))
            self.update_table(jeu, adversaires,InitialTable, InitialAlreadyPlayedCards)
            score = self.score
            print('table dans la boucle contre bot random ',InitialTable,"\n")
            print('table constante ',self.constable,"\n")
            print("le score est : ",score,"\n la carte est : ",card,"\n")
            Diffscore = score - scoreInitial
            if Diffscore <= DifferenceOptimal:
                DifferenceOptimal = Diffscore
                risky_cards.append((card, score))
            adversaires.pop()
            InitialTable = self.constable
            print('table A utiliser dans la boucle contre bot random ',InitialTable,"\n")
            InitialAlreadyPlayedCards= self.constalreadyPlayedCards
            jeu = self.constGame
            self.score = scoreInitial

        if risky_cards:
            print("risky cards",risky_cards)
            least_risky_card = risky_cards[0][0]
            for card in risky_cards:
                if card[1] < risky_cards[0][1]:
                    least_risky_card = card[0]
        else:
            least_risky_card = None

        self.score = scoreInitial

        print("carte avec moin de risque \n",least_risky_card)

        return least_risky_card

        
    def player_turn(self, game):
        self.constGame = copy.deepcopy(game)
        game.table.sort(key=lambda x: x[-1])
        self.constable = copy.deepcopy(game.table)
        print('table constante après assigning value',self.constable)
        self.constalreadyPlayedCards = copy.deepcopy(game.alreadyPlayedCards)
        print("test si deep copy marche ",self.constalreadyPlayedCards)
        print("La table du jeu \n",game.table)
        carteChoisie = Card(self.getCardToPlay())
        print("cette table doit être égale à celle du jeu (non-modifiée) \n",self.constable)
        print('la crate choisie',carteChoisie)
        return carteChoisie

    
