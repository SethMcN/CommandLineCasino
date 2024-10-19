from time import sleep 
from random import randint
from casino_lib import *
from blackjack import draw_line

def dice_rolling_game (balance):
    # define variables --------------------------------------------------
    balance -= 5
    total = 0 
    
    print(f"\n£5 has been deducted your balance is now £{balance}")

    # start game --------------------------------------------------------
    num_of_dice = input("\nHow many dice do you want to play with?: ")

    while num_of_dice.isdigit() == False:
        print("invalid number")
        num_of_dice = input("How many dice do you want to play with?: ")    

    num_of_dice = int(num_of_dice)

    while num_of_dice < 1:
        print("invalid number")
        num_of_dice = input("How many dice do you want to play with?: ")



    while True:
        move = input(f"\nRoll(1) or Withdraw(2)? total = £{total}: ")

        # checking the input --------------------------------------------
        while move.lower() not in ["roll","withdraw","1","2"]:
            print("invalid move")
            move = input(f"Roll(1) or Withdraw(2)? total = £{total}")
        
        if move.lower() in ["2","withdraw"]:
            balance += total 
            print(f"you win £{total} your balance is now £{balance}")
            return balance
        
        elif move.lower() in ["1","roll"]:

            print("rolling dice: ")

            roll_outcome = []

            for i in range(num_of_dice):
                print (".",end="")
                sleep(.2)
                roll = randint(1,6)
                roll_outcome.append(roll)

            print("")
            draw_line()
            print("")

            for ind,roll in enumerate(roll_outcome):
                print(f"for roll {ind+1} you rolled {roll}")
                sleep(.4)

            if 1 in roll_outcome:
                print(f"\nbecause you rolled a 1 on roll {roll_outcome.index(1)+1}") 
                print(f"your lose your total which was £{total}")
                return(balance)
            
            total += sum (roll_outcome)
            