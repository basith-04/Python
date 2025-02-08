import random

choices = ["rock","paper","scissors"]
again = "y"

while again == "y":

    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock, paper or scissors ? ").lower()

    if computer == player:
        print("computer :", computer)
        print("player :", player)
        print("tie")

    elif player == "rock":
        if computer == "paper":
            print("computer :", computer)
            print("player :", player)
            print("computer wins ")
        elif computer == "scissors":
            print("computer :", computer)
            print("player :", player)
            print("player wins")

    elif player == "paper":
        if computer == "rock":
            print("computer :", computer)
            print("player :", player)
            print("player wins")
        elif computer == "scissors":
            print("computer :", computer)
            print("player :", player)
            print("computer wins")
    elif player == "scissors":
        if computer == "rock":
            print("computer :", computer)
            print("player :", player)
            print("computer wins")
        elif computer == "paper":
            print("computer :", computer)
            print("player :", player)
            print("player wins")
    again = input("\n do you want to play agian ? y/n ").lower()
