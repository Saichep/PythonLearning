#!/usr/bin/env python

__author__ = "Sudheer Veeravalli <veersudhir83@gmail.com>"
__copyright__ = "Copyright (c) 2017. Sudheer Veeravalli. Free for general use and re-distribution"
__license__ = "Public Domain"
__version__ = "1.0"

from random import randint

choices = ['R', 'P', 'S']

def random_choice(choices):
    return randint(0, len(choices) - 1)

computer_choice = choices[random_choice(choices)]

print("Computer Choice:", computer_choice)


player_choice = input("Input Your Choice [R/P/S] only: ")
print("Player choice: " , str(player_choice).upper())