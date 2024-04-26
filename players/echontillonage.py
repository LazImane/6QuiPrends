import random
from random import shuffle
from players.player import Player
from game.card import Card
from players.Random import Random
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
        score = game.total_cows(game.table[0])
        for i,row in enumerate(game.table):
            print("the actual score of the line nb ",i,"is :",game.total_cows(row))
            if(score >= game.total_cows(row)):
                print("line nb : ",i,"score : ",score)
                score = game.total_cows(row)
                ligne = i
        print("la ligne : choisie ",ligne)
        return ligne
    
    def echantillon_cartes_adversaires(self):
        """
        echantillon des cartes hypothétiques des adversairess.
        et sous-ensemble de la carte qui peut-être joué par l'adversaire
        cela doit être d'une taille égale aux nombre de joueurs
        """
        print("la main du bot : ", self.hand)
        #print("nombre de joueurs : ",self.nbJoueurs - 1)
        E = [] #contient un sous-ensemble hypothétiques des cartes des adversaires
        #print("testing ... ",E)
        cartesHypothèses = [] #variable pour contenir temporèrement les cartes d'un seul adversaires
        knownCards = self.constalreadyPlayedCards #les cartes déjà connue
        knownCards += self.hand
        cards = list(map(lambda c:Card(c),list(range(1, 105))))
        
        for card in knownCards :
            if card in cards :
                cards.remove(card)
        
        shuffle(cards)
        
        for i in range(self.nbJoueurs-1):
            player = Random()
            for _ in range(len(self.hand)) :
                carte = cards.pop()
                cartesHypothèses.append((player,carte))
            #print("i ",i)
            E.append(cartesHypothèses)
            #print("E after append ",E)
            cartesHypothèses = []
            #print("testing cartesHyp after initialisation",cartesHypothèses)
        
        knownCards = self.constalreadyPlayedCards
        #print("sous-ensemble des cartes hypothèses des adversaires \n",E)
        return E
    
    def checkIfElementInList(self,elem,list):
        """
        on vérifie si elem existe déja dans une liste de tuples (elem,score)
        """
        for card,score in list:
            if card.value == elem.value :
                return True
        return False
    
    def estProche(self,valeur,cible,tolerance):
        return abs(valeur - cible) <= tolerance

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
                #print('line removed is line nb : ',line)
                player.score += game.total_cows(table[line-1])
                table[line - 1] = [card]
                table.sort(key=lambda x: x[-1])

    def find_risky_cards(self,jeu,adversaires,scoreInitial,risky_cards,DifferenceOptimal,
                         InitialTable,InitialAlreadyPlayedCards):
        for card in self.hand:
            adversaires.append((self, card))
            #print("adversaires ",adversaires)
            self.update_table(jeu, adversaires,InitialTable, InitialAlreadyPlayedCards)
            score = self.score
            Diffscore = score - scoreInitial
            if Diffscore <= DifferenceOptimal:
                DifferenceOptimal = Diffscore
                if not(self.checkIfElementInList(card,risky_cards)):
                    risky_cards.append((card, Diffscore))
            adversaires.pop()
            InitialTable = copy.deepcopy(self.constable)
            InitialAlreadyPlayedCards= copy.deepcopy(self.constalreadyPlayedCards)
            jeu = copy.deepcopy(self.constGame)
            self.score = scoreInitial

    def prototype_riky_card(self,risky_cards):
        print("risky cards",risky_cards)
        least_risky_card = risky_cards[len(risky_cards)-1]
        for i in range(len(risky_cards)-1,-1,-1):
            if risky_cards[i][1] <= least_risky_card[1]:
                least_risky_card = risky_cards[i]
        return least_risky_card[0]

    def evaluate_least_risky_card(self, E):
        """
        Evalue la carte la moins risqué à poser
        """
        InitialTable = copy.deepcopy(self.constable)
        InitialAlreadyPlayedCards = copy.deepcopy(self.constalreadyPlayedCards)
        jeu = copy.deepcopy(self.constGame)
        scoreInitial = self.score
        DifferenceOptimal = 0 #le score maximum on peut accepter
        adversaires = []
        risky_cards = []
        cartesOPP = copy.deepcopy(E) #cartes des OPPonents/adversaires
        #print("cartesOPP ",cartesOPP,"\n")
        cond = False

        while cartesOPP :
            adversaires = []
            #print("cartesOPP DAns la boucle WHILE",cartesOPP,"\n")
            for i in range (len(cartesOPP)):
                #print("Type of cartesOPP[i]:", type(cartesOPP[i]))
                #print("Before pop, cartesOPP[i]:", cartesOPP[i])
                if len(cartesOPP[i])==0 and i == len(cartesOPP)-1:
                    cond = True
                if cond :
                    break
                if cartesOPP[i] :
                    elem = cartesOPP[i].pop()
                    #print("elem : ",elem)
                    adversaires.append(elem)
                    #print("cartesOPP APRES POP",cartesOPP,"\n")
                    #print("adversaires ",adversaires)
                else :
                    cartesOPP = []
                    break
            if cond :
                    break
        self.score = scoreInitial
        least_risky_card = 0
        while len(risky_cards)==0:
            self.find_risky_cards(jeu,adversaires,scoreInitial,risky_cards,DifferenceOptimal,
                              InitialTable,InitialAlreadyPlayedCards)
            if risky_cards:
                least_risky_card = self.prototype_riky_card(risky_cards)
                print("carte avec moin de risque \n",least_risky_card)
                return least_risky_card
            else:
                DifferenceOptimal += 1
        
    def player_turn(self, game):
        self.constGame = copy.deepcopy(game)
        game.table.sort(key=lambda x: x[-1])
        self.constable = copy.deepcopy(game.table)
        #print('table constante après assigning value',self.constable)
        self.constalreadyPlayedCards = copy.deepcopy(game.alreadyPlayedCards)
        #print("test si deep copy marche ",self.constalreadyPlayedCards)
        #print("La table du jeu \n",game.table)
        carteChoisie = Card(self.getCardToPlay())
        #print("cette table doit être égale à celle du jeu (non-modifiée) \n",self.constable)
        print('la carte choisie',carteChoisie)
        return carteChoisie
    
    """ ANOTHER APPROACH
    for row in InitialTable :
                    valeur = risky_cards[i][0].value
                    if self.estProche(valeur,row[len(row)-1].value,9) and len(row)<4 :
                        least_risky_card = risky_cards[i]
                        self.score = scoreInitial
                        print("carte avec moin de risque \n",least_risky_card)
                        return least_risky_card[0]
                    elif self.estProche(valeur,row[len(row)-1],3) and len(row)>4:
                        risky_cards.remove(risky_cards[i])
    """

    
