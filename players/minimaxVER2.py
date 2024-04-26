from players.player import Player
from game.card import Card
import math 
import copy  
import random 
#copy.deepcopy(tableaucopie)

class minmaxPlayer(Player) :
    def __init__(self) -> None:
        """
        Crée un joueur avec un nom donné.

        :param name: Le nom du joueur.
        """
        self.name="MINMAXBOT"
        self.score=0
        self.hand=[]
        self.gamestate = []
        self.constalreadyPlayedCards = []
        self.hypotheticaladversairecartes = []

    def info(self, message):
        """
        Affiche un message à l'attention du joueur.
        
        :param message: Le message à afficher.
        """
        print("@"+self.name+" : ",message)

    def get_possible_moves(self, state, maximizing_player ,table_state): #branching of the tree #on ajoute le node aux parametres???
        choices = []
        itérateurs = 0
        if maximizing_player : 
            for card in state : 
                #if card != pere du node
                #print('hihi'+str(table_state))
                potential_score , newtablestate = self.evaluatepotentialscore([(self, card)] , table_state)
                #print("the potential score of the card : " + str(card.value) + " is " + str(potential_score))
                choices.append((card, potential_score,newtablestate))
            #return choices  
        else:
            for i in range (0,len(self.hand)) : 
                #print('hihi'+str(table_state))

                #valeurs non existants a table ou dans les cartes restantes
                card = Card(random.randint(1 , 105)) 
                #while card not in self.hand and card not in table_state :
                #print('card'+ str(card))
                potential_score , newtablestate = self.evaluatepotentialscore([(self , card)] , table_state)
                choices.append((card , potential_score,newtablestate))
        #print('final choices ' , str(choices) , 'table_state' , str(state))
        return choices
    def sort_table(self , list):
        """
        Trie le plateau par ordre croissant des dernières cartes de chaque ligne.
        """
        list.sort(key=lambda x: x[-1])
    def choixadversairepossible(self):
        knownCards = self.constalreadyPlayedCards #les cartes déjà connue
        knownCards += self.hand
        cards = list(map(lambda c:Card(c),list(range(1, 105))))
        
        for card in knownCards :
            if card in cards :
                cards.remove(card)
        

    def evaluatepotentialscore(self , plays , table_state) :
        scoretemp=0
        for player, card in plays:
            #print('premier parcours de la liste')
            placed = False
            for i in range(len(table_state) - 1, -1, -1):
                newtablestate = copy.deepcopy(table_state)

                #print('deuxieme parcours de la liste')
                if table_state[i][-1]<card:
                    if len(table_state[i]) < 5:
                        #print('condition table_state[i]) < 5')
                        newtablestate[i].append(card)
                    else:
                        #print(table_state)
                        cows = sum(card.cowsNb for card in table_state[i])
                        scoretemp+= cows
                        newtablestate[i] = [card]
                        self.sort_table(newtablestate)
                    placed = True
                    break
            if not placed:
                #print("condition not placed")
                line=0
                scoretemp = sum(card.cowsNb for card in table_state[0])
                for i,row in enumerate(table_state):
                    if(scoretemp <= sum(card.cowsNb for card in table_state[i])):
                        line = i
                        ##print(line)
                #line=self.getLineToRemove()
                scoretemp += sum(card.cowsNb for card in table_state[line])
                newtablestate[line - 1] = [card]
                self.sort_table(newtablestate)
            print('score' + str(scoretemp) + 'new table state' + str(newtablestate))
        return scoretemp , newtablestate

        
# appel à minimax(self.hand , game.table , profondeur , +inf, -inf , TRUE)
    def minimax(self , state, table_state,possiblechoices, profondeur , alpha , beta , maxplayer ):
    #def minimax(self, state , table_state , profondeur , maxplayer): 
        if profondeur == 0 :
            print('-----cas de base reached lol !!!!§§§§!!!§§§§')
            print('ùùmmmmmdùqsmùsqpmlCONFZETOIJààà@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            #print('possiblechoices' + len(possiblechoices))
            #return state[0].value #retourner la carte du node concerne
            print(possiblechoices[0][1])
            self.possiblechoices = possiblechoices
            return possiblechoices[0][1]
        
        if maxplayer: 
            value = float('inf')
            possiblemoves = self.get_possible_moves( state, maxplayer, table_state)
            print('possible moves of ' + str(state) + 'is :' + str(possiblemoves)) 
            for child,card, tablestate in possiblemoves:
                print('parcourir la liste possible moves'); 
                current_state = copy.deepcopy(state)
                current_state.remove(child)
                print("current_state" , str(current_state))
                value = min((value) , int(self.minimax(current_state ,tablestate, possiblemoves,profondeur -1 , alpha , beta , False)))
                print('*****value after boucle' + str(value))
                beta = min(beta , value)
                if value <= alpha :
                    break
            return value

                #value = max(int(value) , int(self.minimax(current_state ,tablestate, profondeur -1 , False)))
                
        else :
            value = float('-inf')          
            possiblemoves= self.get_possible_moves( state, maxplayer, table_state)
            print('possible moves of ' + str(state) + 'is :' + str(possiblemoves))
            #definir childmax 
            for child,card,tablestate in possiblemoves:
                print('parcourir la liste possible moves minimiser!!!'); 
                current_state = copy.deepcopy(state)
                current_state.remove(child)
                print("current_state" , str(current_state))
                value = max(value , int(self.minimax(current_state ,tablestate,possiblemoves,  profondeur -1 , alpha , beta , True)))
                #value = min(int(value) , int(self.minimax(current_state ,tablestate,  profondeur -1 , True)))
                print('*****value after boucle' + str(value))
                if value >= beta : 
                    break 
                alpha = max(alpha, value)
            return value
    def evaluate(self, state):
        minchoix = state[0]
        for i in range(1, len(state)) :
            if state[i][1] <= minchoix[1]:
                minchoix = state[i][1]
        return minchoix[0]
            
    
    def player_turn(self, game):
        """
        Gère le tour de jeu d'un joueur.

        :param game : le jeu en cours
        """
        self.gamestate = copy.deepcopy(game.table) 
        self.constalreadyPlayedCards = copy.deepcopy(game.alreadyPlayedCards)

        self.info(game.display_scores())
        self.info(game.display_table())
        while True:
            self.info(f"Votre main : {' '.join(map(str, self.hand))}")
            try:
                #initial_state = [(Card(10), 5), (Card(20), 8), (Card(30), 3)]  # Example initial state
                if(len(self.hand) <= 2) : 
                    carteChoisie = self.hand[0]
                else:
                    self.scoremin = (self.minimax(self.hand  , self.gamestate ,[], 3 , float('inf') , float('-inf') , True))
                    print('MINIMAX SCORE MIN' + str(self.scoremin))
                    carteChoisie = (self.getCardToPlay())
                    print('WELL ???? CARTE CHOISI' + str(carteChoisie))
                #print('sjkslsLDKSMDSLK' + str(self.minimax(self.hand  , game.table , 3 , True)))
                #carteChoisie = Card(self.minimax(self.hand  , game.table , 3 , True))
                print('CARTE CHOISI9999DSµSµDSµSDµ' , str(carteChoisie))

                if carteChoisie in self.hand:
                    print('carte retournee.')
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
        #self.game = game.table
        print(game.table)
 
        for i,row in enumerate(game.table):
            scoret = game.total_cows(row)
            if(scoret <= game.total_cows(row)):
                ligne = i
                print(ligne)
        return ligne 
    def getCardToPlay(self):
        print('OK OK SO MAYBE POSSIBLE CHOICES IS THE PROBLEM ' + str(self.possiblechoices))
        cartechoisi = 0
        for card, score, state in self.possiblechoices : 
            print('card ' + str(card) + 'score ' + str(score))
            if score == self.scoremin and card in self.hand: 
                cartechoisi = card
                break 
        else: 
            cartechoisi = card[0]
        print('carte choici finale ççç' , str(cartechoisi))
        return cartechoisi



