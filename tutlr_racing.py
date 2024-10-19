import turtle 
from time import sleep
import random

colours = ["blue","red","green","orange","purple"]

width,height = 500,750

def draw_line():
    print("-------------------------------------------------------------------")

def win(winner):

    width,height = 500,500

    # sets screen ---------------------------------------
    turtle.clearscreen()
    turtle.bgcolor("#faf9d7")
    screen = turtle.Screen()
    screen.setup(width,height)
    screen.title("Turtle racing winners!")
    
    box = turtle.Turtle()
    box.penup()
    box.speed(0)
    box.setpos(-width//2+20,-height//2+10)
    box.left(90)
    box.pendown()
    #second place box ------------------------------
    box.forward(170)
    box.right(90)
    box.forward(150//2)
    secondx,secondy = box.pos()
    box.forward(150//2)
    #first place box ------------------------------
    box.left(90)
    box.forward(130)
    box.right(90)
    box.forward(150//2)
    firstx,firsty = box.pos()
    box.forward(150//2)
    box.right(90)
    box.forward(170)
    #third place box --------------------------------
    box.left(90)
    box.forward(150//2)
    thirdx,thirdy = box.pos()
    box.forward(150//2)
    box.right(90)
    box.forward(150)
    # 3rd place ------------------------------------
    sleep(.5)
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.shapesize(1.75, 1.75, 1)
    racer.left(90)
    racer.color(colours[winner[2]])
    racer.penup()
    racer.setpos(thirdx,thirdy+50)
    # 2nd place ------------------------------------
    sleep(.5)
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.shapesize(1.75, 1.75, 1)
    racer.left(90)
    racer.color(colours[winner[1]])
    racer.penup()
    racer.setpos(secondx,secondy+50)
    # 1st place ------------------------------------
    sleep(.5)
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.shapesize(1.75, 1.75, 1)
    racer.left(90)
    racer.color(colours[winner[0]])
    racer.penup()
    racer.setpos(firstx,firsty+50)
    
    turtle.exitonclick()

# creates the window -------------------------------------
def init_tur ():
    screen = turtle.Screen()
    turtle.TurtleScreen._RUNNING=True
    turtle.clearscreen()
    turtle.bgcolor("#faf9d7")
    
    screen.setup(width,height)
    screen.title("Turtle racing!")

# creates each racer --------------------------------------
def create_racer (colours):
    race_track ()
    turtles = []
    for i,colour in enumerate(colours):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.shapesize(1.75, 1.75, 1)
        racer.color(colour)
        racer.left(90)
        racer.penup()
        racer.setpos(-width//2 + (i+.5) * width//5+1,-height//2+30)
        racer.pendown()
        turtles.append(racer)
    return (turtles)

def race_track ():
    # finish line ------------------------------------------------
    finish = turtle.Turtle()
    finish.hideturtle()
    finish.color('black')
    finish.speed(0)
    finish.penup()
    finish.setpos(-width//2, height//2 - 20)
    finish.pendown()
    finish.forward(width)
    # columns --------------------------------------------------
    column = turtle.Turtle()   
    column.hideturtle()
    column.color('black')
    column.speed(0) 
    column.left(90)
    for i in range (5):
        column.penup()
        column.setpos((-width//2 + (i+.5) * width//5+1)+50,-height//2+20)
        column.pendown()
        column.forward(height-40)

def race ():
    init_tur()
    turtles = create_racer (colours)
    turtles_2 = turtles.copy()
    order_of_winners = []
    while True:
        for racer in turtles_2:

            if racer != "empty":
                racer.forward(random.randint(1,20))

                x,y = racer.pos()
            else:
                y = 0

            if y >= height//2 -10:
                winner = turtles.index(racer)
                order_of_winners.append(winner)
                turtles_2[winner] = "empty"
                if len(order_of_winners) > 4:
                    sleep(1)
                    win(order_of_winners)

                    return(order_of_winners)


def game_start (balance):
    draw_line()
    print("To start which turtle do you want to bet on?:\n")

    for i,colour in enumerate(colours):
        print(f"{i+1}:{colour}")
        sleep (.3)

    racer = input("\nWhich racer do you want to bet on?: ") or "N/A"
    player_input = "invalid"
    while True:       

        for num,colour in list(enumerate(colours)):

            if racer.isdigit():
                if int(racer) == num+1:
                    player_input = "valid"

            if racer.lower() == colour:
                player_input = "valid"

        if player_input == "invalid":
            print("\nPlease bet on a valid racer\n")
            racer = input("Which racer do you want to bet on?: ") or "N/A"

        if player_input == "valid":
            break

    if racer.isdigit():
        for num,colour in list(enumerate(colours)):
            if int(racer)-1 == num:
                racer = colour
                break

    racer = racer.lower()
    
    bet = input(f"\nHow much do you want to bet on {racer} (balance = £{balance}): £")

    player_bet = "invalid"

    while player_bet == "invalid":

        if bet.isdigit():
            bet = int(bet)
            if bet <= balance and bet > 0:
                player_bet = "valid"
        
        if player_bet != "valid":
            print("invalid bet")
            bet = input(f"How much do you want to bet on {racer}: £")

    balance -= bet

    order_of_winners = (race ())

    draw_line()
    sleep(.5)
    if racer == colours[order_of_winners[0]]:
        print (f"{colours[order_of_winners[0]]} came first 2x multiplier has been applied you win £{bet*2}")
        bet *= 2

    elif racer == colours[order_of_winners[1]]:
        print (f"{colours[order_of_winners[1]]} came second a 1.5x multiplier has been applied you win £{bet*1.5}")
        bet *=1.5

    else:
        position = order_of_winners.index(colours.index(racer))+1

        if position == 3: position = "3"+"rd"

        else: position = str(position)+"th"

        print(f"Your racer came {position} this means you lose £{bet}")
        bet -= bet

    return (balance+bet)

def Turtle_racing_game(balance):
    balance = game_start(balance)
    return balance
