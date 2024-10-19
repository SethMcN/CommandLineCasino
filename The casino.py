from casino_lib import *
from blackjack import *
from tutlr_racing import *
from dice_betting import *
from slots import *
from save_game_class import *

balance = 100

print("""
---Welcome to the casino---
      
---You start with £100---
      
---Feel free to play any game--- \n""")

while True:
    for i in range (1,len(different_games)+1):
        print (f"{i}: {different_games[i-1]}")
        sleep(.3)

    game = input("\nWhich game do you want to play?: ").lower()

    if game == "balance":
        print(balance)

    elif game == "dev123":
        balance += 9999999

    elif game == "1" or game == "blackjack":
        balance = blackjack_game(balance)
        print (f"Your balance is now £{balance}\n")
        draw_line()

    elif game == "2" or game == "turtle racing":
        balance = Turtle_racing_game(balance)
        print (f"Your balance is now £{balance}\n")
        draw_line()

    elif game == "3" or game == "dice rolling":

        if rules_read == False:

            print("\n______Rules______\n")

            for i in dice_rules:
                sleep(.01)
                print(i,end = "")

            rules_read = True

            option = input("\nDo you want to play?(Y/N): ").lower()

            if option in ["y","yes"]:
                balance = dice_rolling_game(balance)

        else:
            balance = dice_rolling_game(balance)
        
        print (f"\nYour balance is now £{balance}\n")

        draw_line()

    elif game == "4" or game == "slots":
        balance = spins_slots_game(balance)
        print (f"\nYour balance is now £{balance}\n")
        draw_line()

    elif game == "save":
        Save(balance,123)

    if balance <= 0:
        print ("Thanks for coming to the casino but you've gone bankrupt\n") 
        exit()
