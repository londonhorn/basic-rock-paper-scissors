
from random import randint

turn = ["Rock", "Paper", "Scissors"]  # three options in a list

computer = turn[randint(0,2)]  # computers turn, picks a random option

player = False  # giving player a false value to make the while loop assign True to the player

while player == False:
    player == input("Rock, Paper, or Scissors? ")
    if player == computer:
        print("It's a tie.")
    elif player == "Rock":
        if computer == "Paper":
            print("The computer plays " + computer + " which covers " + player + " , you lose.")
        if computer == "Scissors":
            print("The computer plays" + computer + " which is smashed by " + player + " , you win.")
    elif player == "Paper":
        if computer == "Scissors":
            print("The computer plays " + computer + " which cuts " + player + " , you lose.")
        if computer == "Rock":
            print("The computer plays" + computer + "which is covered by " + player + " , you win.")
    elif player == "Scissors":
        if computer == "Rock":
            print("The computer plays " + computer + "which smashes " + player + " , you lose.")
        if computer == "Paper":
            print("The computer plays" + computer + "which is cut by " + player + " , you win.")
    else:
        print("Not a valid play. Check your spelling.")

player = False
computer = turn[randint(0,2)]

