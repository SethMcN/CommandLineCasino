from time import *
from random import *
from casino_lib import *


def slots_setup():
    #creates a list with different number of symbols to control probabilities 
    symbols_odds_list = create_symbol_list()
    return symbols_odds_list

def create_symbol_list ():

    symbols_odds_list = []

    for symbol,amount in symbols.items():
        for i in range(amount):
            symbols_odds_list.append(symbol)

    return symbols_odds_list 

def spins_slots_game(balance):
    print("Each spin costs £10")
    sleep(.5)
    good_to_go = "no"

    while good_to_go == "no":
        sleep(.5)

        try:
            num_of_spins = int(input("enter the number of spins you want to play: "))

            if num_of_spins < 1:
                print("please enter a number greater then 0\n")
            else:
                print(f"\nYour total is £{num_of_spins*10} this leaves you with £{balance-num_of_spins*10}")
                
                while True:
                    ans = input("Do you want to continue?(y/n): ")

                    if ans.lower() in ["y","yes"]:
                        good_to_go = "yes"
                        break

                    elif ans.lower() in ["n","no"]:
                        break

        except ValueError:
            print("only enter whole numbers\n")

    balance -= num_of_spins * 10
    print("")
    while num_of_spins > 0 :

        spins,money = slots_game()

        num_of_spins += spins
        balance += money
        num_of_spins -= 1

        draw_line()
        print(f"Winnings = £{money}")
        sleep(.3)
        print(f"balance = £{balance}")
        sleep(.3)
        print(f"spins left = {num_of_spins}")
        draw_line()
        sleep(.3)

        if num_of_spins != 0:
            input("\nPress enter to continue")

        else:
            return balance
        
def slots_game():
    ROWS_ = 5


    # controls the speed of the wheel as it gradualy gets slower 
    delay = 0
    while delay <= 1:

        sleep(delay)
        slot_outcome = []

        symbols_odds_list = slots_setup()

        for i in range(ROWS_):
            slot_outcome.append(choice(symbols_odds_list))

        for smbol in slot_outcome:
            print (f"|{smbol}|",end = "")

        print("")
        if delay > .25:    
            delay += .25

        else:                 
            delay += .008
    
    # generates final outcome ---------------------------------------
    draw_line()
    slot_outcome = []

    for i in range(ROWS_):
            slot_outcome.append(choice(symbols_odds_list))
    for smbol in slot_outcome:
            print (f"|{smbol}|",end = "")

    print("")
    draw_line()
    # --------------------------------------------------------------

    total_run = []
    symbol_count = []
    end_point = 1
    count = 1
    # calculates the num of max number of consecutive symbols in a line and which symbol it is 

    slot_outcome_copy = slot_outcome.copy()

    removed_symbol = slot_outcome_copy[len(slot_outcome_copy)-1]
    del slot_outcome_copy[len(slot_outcome_copy)-1]

    for i in range (len(slot_outcome)-2,-1,-1):

        if slot_outcome_copy[i] == removed_symbol:
            count += 1

        else:
            total_run.append(count)
            symbol_count.append(removed_symbol)
            count = 1

        removed_symbol = slot_outcome_copy[i]
        del slot_outcome_copy[i]


               
    symbol_count.append(removed_symbol)           
    total_run.append(count)


    if max(total_run) < 3:
        print ("\nNo line :( ")
        spins,money = 0,0
     
    else:
        max_row = max(total_run) 
        max_symbol = symbol_count[total_run.index(max(total_run))]
        sleep(.3)
        print(f"\nmax row = {max_row}")  
        
        print(f"with symbol = {max_symbol}") 

        #checks in slot_checker function ---------------------------
        spins,money = slot_checker(max_row,max_symbol)


    return spins,money
def slot_checker(max_row,max_symbol):
        spins,money = 0,0
        # if max spin is 3 and symbol is 🤩/ most common symbol then win free spin
        if max_row == 3 and max_symbol == list(symbols)[0]: 
            sleep(.3)
            print("You won a free spin!!!")
            spins += 1

        # if max spin is 4 and symbol is 🤩/ most common symbol then win free spin + small payout 
        elif max_row == 4 and max_symbol == list(symbols)[0]:
            sleep(.3)
            print(f"You won a free spin + £{slot_cost*small_payout}!!!")
            money += slot_cost*small_payout
            spins += 1

        # if max spin is 5 and symbol is 🤩/ most common symbol then win free spin + medium payout 
        elif max_row == 5 and max_symbol == list(symbols)[0]:
            sleep(.3)
            print(f"You won a free spin + £{slot_cost*med_payout}!!!")
            money += slot_cost*med_payout
            spins += 1

        # if max spin is 3 and symbol is 👺🤑💀 then small pay
        elif max_row == 3 and max_symbol in list(symbols)[1:4]: 
            sleep(.3)
            print(f"£{slot_cost*small_payout}!!!")
            money += slot_cost*small_payout

        # if max spin is 4 and symbol is 👺🤑💀 then med pay
        elif max_row == 4 and max_symbol in list(symbols)[1:4]:
            sleep(.3)
            print(f"£{slot_cost*med_payout}!!!")
            money += slot_cost*med_payout

        # if max spin is 5 and symbol is 👺🤑💀 then large pay
        elif max_row == 5 and max_symbol in list(symbols)[1:4]:
            sleep(.3)
            print(f"£{slot_cost*l_payout}!!!")
            money += slot_cost*l_payout

        # if max spin is 3 and symbol is 👽🎃🤖 then med pay
        elif max_row == 3 and max_symbol in list(symbols)[4:7]: 
            sleep(.3)
            print(f"£{slot_cost*med_payout}!!!")
            money += slot_cost*med_payout

        # if max spin is 4 and symbol is 👽🎃🤖 then med pay
        elif max_row == 4 and max_symbol in list(symbols)[4:7]:
            sleep(.3)
            print(f"£{slot_cost*l_payout}!!!")
            money += slot_cost*l_payout


        # if max spin is 5 and symbol is 👽🎃🤖 then large pay
        elif max_row == 5 and max_symbol in list(symbols)[4:7]:
            sleep(.3)
            print(f"£{slot_cost*xl_payout}!!!")
            money += slot_cost*xl_payout
        
        # if max spin is 3 and symbol is 👾 then med pay
        elif max_row == 3 and max_symbol in list(symbols)[7]: 
            sleep(.3)
            print(f"£{slot_cost*xxl_payout}!!!")
            money += slot_cost*xxl_payout

        # if max spin is 4 and symbol is 👾 then med pay
        elif max_row == 4 and max_symbol in list(symbols)[7]:
            sleep(.3)
            print(f"£{slot_cost*super_pay}!!!")
            money += slot_cost*super_pay

        # if max spin is 5 and symbol is 👾 then large pay
        elif max_row == 5 and max_symbol in list(symbols)[7]:
            sleep(.3)
            print(f"£{slot_cost*jackpot}!!!")
            money += slot_cost*jackpot

        return spins,money

