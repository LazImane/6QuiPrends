
from players.humanPlayer import HumanPlayer
from game.nimmtGame import NimmtGame  
from players.medianCardBot import MedianCardBot 
from players.theWeak import TheWeak  
from players.echantillionage import Echantillions
from players.minmax import minmaxPlayer 
from players.carteplusfort import CartePlusForte
from players.random import Random
import matplotlib.pyplot as plt

def playMultipleGames(num_games):
    # Initialiser un dictionnaire pour stocker le nombre de victoires par bot
    victoires_par_strategie = {
        "Random": 0,
        "TheWeak": 0,
        "MedianCardBot": 0,
        "Echantillions": 0,
        "minmaxPlayer":0,
        "CartePlusForte":0
    }
    num_players = int(input("Combien de joueurs?"))
    for _ in range(num_games):
        players = [
            Random(),
            TheWeak(),
            MedianCardBot(),
            Echantillions(num_players),
            minmaxPlayer(),
            CartePlusForte()
        ]
        game = NimmtGame(players)
        scores, winners = game.play()
        
        # Mettre à jour le nombre de victoires pour chaque stratégie
        for player in winners:
            if isinstance(player, Random):
                victoires_par_strategie["Random"] += 1
            elif isinstance(player, TheWeak):
                victoires_par_strategie["TheWeak"] += 1
            elif isinstance(player, MedianCardBot):
                victoires_par_strategie["MedianCardBot"] += 1
            elif isinstance(player, Echantillions):
                victoires_par_strategie["Echantillions"] += 1
            elif isinstance(player,minmaxPlayer):
                victoires_par_strategie["minmaxPlayer"] += 1
            elif isinstance(player,CartePlusForte):
                victoires_par_strategie["CartePlusForte"] += 1

    print("Nombre de victoires par stratégie :")
    for strategie, victoires in victoires_par_strategie.items():
        print(f"{strategie}: {victoires} victoire(s)")
    

    # the graph
    strategies = list(victoires_par_strategie.keys())
    victoires = list(victoires_par_strategie.values())

    plt.bar(strategies, victoires, color=['#4287f5', '#ff9c00', '#23c48e', '#d33682'])
    plt.xlabel("Stratégies", fontsize=12, fontweight='bold')
    plt.ylabel("Nombre de victoires", fontsize=12, fontweight='bold')
    plt.title("Nombre de victoires gagnées par bot", fontsize=14, fontweight='bold')

    # Personnaliser les étiquettes des axes x et y
    plt.xticks(fontsize=8, rotation=90) 

    plt.tight_layout() 

    plt.show()

if __name__ == "__main__":
    num_games = int(input("Combien de parties souhaitez-vous jouer ? "))
    playMultipleGames(num_games)

