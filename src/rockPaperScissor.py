#!/usr/bin/env python

__author__ = "Sudheer Veeravalli <veersudhir83@gmail.com>"
__copyright__ = "Copyright (c) 2017. Sudheer Veeravalli. Free for general use and re-distribution"
__license__ = "Public Domain"
__version__ = "1.0"

from random import randint

choices = ['ROCK', 'PAPER', 'SCISSOR']

computer_choice = choices[randint(0,2)].upper()

for turn in range(1, 4):
    print("Turn", turn, "of 3")

    player_choice = str(input("Input Your Choice [ ROCK | PAPER | SCISSOR ] only: ")).upper()
    print("Your choice: " , player_choice)

    if player_choice == computer_choice:
        print("Tie!")
    elif player_choice == "ROCK":
        if computer_choice == "PAPER":
            print("Computer Choice:", computer_choice)
            print("You lose!", computer_choice, "covers", player_choice)
        else:
            print("You win!", player_choice, "smashes", computer_choice)
    elif player_choice == "PAPER":
        if computer_choice == "SCISSOR":
            print("Computer Choice:", computer_choice)
            print("You lose!", computer_choice, "cut", player_choice)
        else:
            print("You win!", player_choice, "covers", computer_choice)
    elif player_choice == "SCISSOR":
        if computer_choice == "ROCK":
            print("Computer Choice:", computer_choice)
            print("You lose...", computer_choice, "smashes", player_choice)
        else:
            print("You win!", player_choice, "cut", computer_choice)
    else:
        print("That's not a valid play. Check your spelling!")
    computer_choice = choices[randint(0,2)].upper()
    print("==================================")
