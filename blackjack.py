# import from other python files ----------------------

import random 
from casino_lib import *
from time import sleep



def draw_line():
    print("-------------------------------------------------------------------")

def totaling (cards,bg_cards):
    total = 0
    for i in bg_cards:
    
        if len(i) == 3:
            total += int(i[0])

        elif len(i) == 4:
            total += int(i[0:2])

        # and ace can be 11 or 1 so if you go above 21 it asumes you want it to be 1 

        if total > 21: 
            if bg_cards == bg_dealer:
                for i in range (len(bg_dealer)):
                    if "11" in bg_dealer[i]:
                        total -= 10 
                        bg_dealer[i] = bg_dealer[i].replace("11", "1",1)

            elif bg_cards == bg_player:
                for i in range (len(bg_player)):
                    if "11" in bg_player[i]:
                        total -= 10 
                        bg_player[i] = bg_player[i].replace("11", "1",1)

    return (total)

def winner (d_total,p_total):
    
    if p_total > d_total or dealer_bust == True:

        print("\nYou win!!!") 
        sleep(.5)       
        print(f"you scored {p_total}")
        sleep(.5)  
        print(f"the dealer scored {d_total}")
        sleep(.5) 
        print(f"£{bet*2} has been added to your acount")

        return(bet*2)
    
    else:

        print(f"\nYou lose :(") 
        sleep(.5)      
        print(f"you scored {p_total}")
        sleep(.5)  
        print(f"the dealer scored {d_total}")
        sleep(.5)  
        print(f"you lost £{bet}")

        return(0)


def card_conversion (p_or_b_cards,bg_cards):

    # sets background cards to j,k,q to 10 and ace to 11---------------------------------------------
    for i in range(len(p_or_b_cards)):
        bg_cards[i] = bg_cards[i].replace("A", "11")
        bg_cards[i] = bg_cards[i].replace("J", "10")
        bg_cards[i] = bg_cards[i].replace("Q", "10")
        bg_cards[i] = bg_cards[i].replace("K", "10")
                

def blackjack_game_add_card(player_or_dealer,bg_set):
    # creates a background set of cards to deal with ace's,king's etc... -------------
    card = b_cards[0]
    player_or_dealer.append(card)
    bg_set.append(card)
    b_cards.remove(card)

def blackjack_game(balance):
    # global variables --------------------------------------------------------------
        # player variables ----------------------------------------------------------
    global player_cards
    global bg_player
    bg_player = []
    player_cards = []
    p_total = 0
        # dealer variables ----------------------------------------------------------
    global bg_dealer
    global dealers_cards
    global dealer_bust
    bg_dealer = []
    dealer_bust = False
    dealers_cards = []
    d_total = 0
        # card variables + game ------------------------------------------------------------
    global b_cards
    global bet 
    b_cards = cards.copy()
    
    # game text + bet from casino_lib ---------------------------------------------------------------
    print("")
    balance,bet = bet_amount(balance)
    print("")
    print("Shuffling the deck")

    # shuffle animation -------------------------------------------------------------

    for i in range (7):
        print(".",end="")
        sleep (.5)

    print(" ")
    random.shuffle(b_cards)

    # first player card -------------------------------------------------------------
    blackjack_game_add_card(player_cards,bg_player)

    # first dealer card -------------------------------------------------------------
    blackjack_game_add_card(dealers_cards,bg_dealer)

    # second player card ------------------------------------------------------------
    blackjack_game_add_card(player_cards,bg_player)

    # second dealer card -------------------------------------------------------------
    blackjack_game_add_card(dealers_cards,bg_dealer)




    # converts non number cards to their real value

    card_conversion (player_cards,bg_player)
    card_conversion (dealers_cards,bg_dealer)

    # prints the cards ---------------------------------------------------------------


    print(f"""
------------------------------------
The game has now begun
------------------------------------""")
    sleep(.5)
    print(f"""
dealer's cards:
        hidden
        {dealers_cards[1]}""")
    sleep(.5)
    print(f"""
player's cards:
        {player_cards[0]}
        {player_cards[1]}
        total = {totaling(player_cards,bg_player)}""")
    draw_line()
    

    # sets two variable to help with the while loop 
    print("")
    satisfide = "no"
    lost = "not yet"
    # while the player still wants more cards or busts 
    while satisfide == "no" and lost == "not yet":
        move = input ("do you want to hit or stand?: ")
        # error checking
        while move.lower() not in ("hit","stand"):
            print("Invalid move")
            move = input ("do you want to hit or stand?: ")
        # if the player wants another card 
        if move.lower() == "hit":
            # adds the card to the players hand and the background player hand the removes it from the deck
            
            blackjack_game_add_card(player_cards,bg_player)

            # converts non number cards to their real value

            card_conversion (player_cards,bg_player)

            # adds up the value of the cards for the player
            p_total = totaling(player_cards,bg_player)


            # prints the players cards
            print("player's cards:")
            for i in player_cards:
                 print(f" :{i}")
                 sleep(.2)
            print(f"total is {p_total}")
            # if the cards total is greater then 21 the player busts 
            if p_total > 21:
                 lost = "yes"
                 break 
            
            draw_line()

        elif move.lower() == "stand":
             p_total = totaling(player_cards,bg_player)
             satisfide = "yes"

    if lost == "yes":
         sleep(.5)
         print (f"YOU BUSTED with {p_total} :( the dealer wins and you lose £{bet}")
         sleep(.5)
         return(balance) 
    
# dealers go ----------------------------------------------------------------------------
    
    while d_total < 17:
            
            # adds up the value of the cards 
            d_total = totaling(dealers_cards,bg_dealer)
        
            if d_total < 17:
                blackjack_game_add_card(dealers_cards,bg_dealer)
            # converts non number cards to their real value
                card_conversion (dealers_cards,bg_dealer)
            # prints dealers cards
                sleep(.5)
            print("\ndealers's cards:")
            for i in dealers_cards:
                 print(f" :{i}")
                 sleep(.7)
            print(f"total is {d_total}")
            
    if d_total > 21 :
        dealer_bust = True
        print("")
        print (f"The dealer busted with {d_total}")

    winings=winner(d_total,p_total)
    return(balance+winings)        
