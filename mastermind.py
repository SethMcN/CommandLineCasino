from random import randint 
from casino_lib import bet_amount
import pygame as py 


def check(player,master):

    right_space = 0
    right_colour = 0 

    # check for direct pairs seperate because of cases like P=8,8,8,8, M=8,8,7,8 would return RR=2,RW=1 insted of RR=3,RW=0 ------------------
    for i in range(len(player)):

        if player[i] == master[i]:
            right_space += 1
            player[i],master[i] = "P","M"

    # check for separeted pairs ----------------------
    # set in while loop to update the player for loop 
    check_compleate = False
    while check_compleate == False:
        check_compleate = True

        for ind_p,colour_p in enumerate(player):
            for ind_m,colour_m in enumerate(master):

                if colour_p == colour_m:
                    player[ind_p],master[ind_m] = "P","M"
                    check_compleate = False
                    right_colour += 1


    return (f"{right_colour=},{right_space=}")


print(check(["B","B","R","G"],["B","R","Y","B"]))



def master_mind_game(balance):
    balance,bet=bet_amount(balance) 
    print(f"For this game of mastermind we will use ({"B","R","G"})")
    for i in range(20):
        guess = input("Please enter guess {i}: ")

    