from players.humanPlayer import HumanPlayer
from game.nimmtGame import NimmtGame     

def interactiveRun():
    print("Bienvenue sur le jeu 6 qui prend !")
    while True:
        try:
            num_players = int(input("Combien de joueurs ? "))
            players=[]
            for i in range(num_players):
                player_type = input(f"Type du joueur {i+1} (humain ou bot) : ").lower()
                if player_type == 'humain':
                    name = input("Nom du joueur : ")
                    players.append(HumanPlayer(name))
                elif player_type == 'bot':
                    print("Veuillez choisir parmi les bots suivants : goat, moat, poat, zut, roat, loo")
                    bot_choice = input("Nom du bot : ").lower()
                    if bot_choice == 'goat':
                        players.append(None)  #remplace None with goat class
                    elif bot_choice == 'moat':
                        players.append(None)   #remplace None with poat class
                    elif bot_choice == 'poat':
                        players.append(None)   #remplace None with poat class
                    elif bot_choice == 'zut':
                        players.append(None)   #remplace None with zut class
                    elif bot_choice == 'roat':
                        players.append(None)   #remplace None with roat class
                    elif bot_choice == 'loo':
                        players.append(None)    #remplace None with loo class
                else:
                    print("Type de joueur invalide. Veuillez entrer 'humain' ou 'bot'.")
                    return
            game=NimmtGame(players)
            scores, winners=game.play()

            print("La partie est terminée!")
            print("Scores finaux :")
            for playername, score in scores.items(): 
                print(f"Joueur {playername} : {score} points")
            s=" ".join([player.name for player in winners])
            print("Vainqueurs(s) : ",s," !")
            break
        except ValueError:
            print("Veuillez entrer un nombre entier.")

if __name__ == "__main__":
    interactiveRun()
