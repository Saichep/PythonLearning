#!/usr/bin/env python

__author__ = "Sudheer Veeravalli <veersudhir83@gmail.com>"
__copyright__ = "Copyright (c) 2017. Sudheer Veeravalli. Free for general use and re-distribution"
__license__ = "Public Domain"
__version__ = "1.0"

from random import randint

choices = ['ROCK', 'PAPER', 'SCISSORS']

def random_choice(choices):
    return randint(0, len(choices) - 1)

computer_choice = choices[randint(0,2)].upper()
#print("Computer Choice:", computer_choice)

player_choice = str(input("Input Your Choice [ ROCK | PAPER | SCISSORS ] only: ")).upper()
print("Your choice: " , player_choice)

if player_choice == computer_choice:
    print("Tie!")
elif player_choice == "ROCK":
    if computer_choice == "PAPER":
        print("You lose!", computer_choice, "covers", player_choice)
    else:
        print("You win!", player_choice, "smashes", computer_choice)
elif player_choice == "PAPER":
    if computer_choice == "SCISSORS":
        print("You lose!", computer_choice, "cut", player_choice)
    else:
        print("You win!", player_choice, "covers", computer_choice)
elif player_choice == "SCISSORS":
    if computer_choice == "ROCK":
        print("You lose...", computer_choice, "smashes", player_choice)
    else:
        print("You win!", player_choice, "cut", computer_choice)
else:
    print("That's not a valid play. Check your spelling!")
