def draw_line():
    print("-------------------------------------------------------------------")

def bet_amount(balance):
    while True:
        bet = input(f"To start the game how much do you want to bet?(balance = £{balance}): £")

        if bet.lstrip('-').isdigit():
            bet = int(bet)
            if bet < 0 or bet > balance:
                print (f"The bet has to be beteen £1 - £{balance}\n")
            
            if bet >= 1 and bet <= balance:
                return balance - int(bet),bet
            
        elif type(bet) == str:   
            print("Please enter a number\n")
            


different_games = ["blackjack","Turtle racing","Dice rolling","Slots"]

cards = ["A,♠","2,♠","3,♠","4,♠","5,♠","6,♠","7,♠","8,♠","9,♠","10,♠","J,♠","Q,♠","K,♠",
         "A,♥","2,♥","3,♥","4,♥","5,♥","6,♥","7,♥","8,♥","9,♥","10,♥","J,♥","Q,♥","K,♥",
         "A,♣","2,♣","3,♣","4,♣","5,♣","6,♣","7,♣","8,♣","9,♣","10,♣","J,♣","Q,♣","K,♣",
         "A,♦","2,♦","3,♦","4,♦","5,♦","6,♦","7,♦","8,♦","9,♦","10,♦","J,♦","Q,♦","K,♦",]

dice_rules=("""For every roll of a dice the number on the dice will get added to the total score
at any time you can end the game and you will be return the total in money
However, if the dice rolls a 1 you lose everything.
\nthere is a £5 minimum entry fee""")

symbols = {"🤩":150,
           "👺":80,
           "🤑":40,
           "💀":40,
           "👽":20,
           "🎃":20,
           "🤖":20,
           "👾":10}

# slots_payouts---------------------------------
slot_cost = 10

small_payout = .5
med_payout = 1.5
l_payout = 2
xl_payout = 3
xxl_payout = 5
super_pay = 10
jackpot = 100
#-----------------------------------------------

rules_read = False

dice1 = ("""
-----
|   |
| o |
|   |
-----""")

dice2 = ("""
-----
|o  |
|   |
|  o|
-----""")

dice3 = ("""
-----
|o  |
| o |
|  o|
-----""")

dice4 = ("""
-----
|o o|
|   |
|o o|
-----""")

dice5 = ("""
-----
|o o|
| o |
|o o|
-----""")

dice6 =("""
-----
|o o|
|o o|
|o o|
-----""")

