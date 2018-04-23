#!/usr/bin/env python

__author__ = "Sudheer Veeravalli <veersudhir83@gmail.com>"
__copyright__ = "Copyright (c) 2017. Sudheer Veeravalli. Free for general use and re-distribution"
__license__ = "Public Domain"
__version__ = "1.0"

from random import randint

board = []

# Initializes the board
for x in range(5):
    board.append(["O"] * 5)


# prints the board
def print_board(board):
    for row in board:
        print(" ".join(row))


print_board(board)


def random_row(board):
    return randint(1, len(board))


def random_col(board):
    return randint(1, len(board[0]))


ship_row = random_row(board)
ship_col = random_col(board)
# print("Ship Co-Ordinates:", ship_row, ship_col)


# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(1, 4):
    print("Turn", turn, "of 3")
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if guess_row not in range(6) or guess_col not in range(6):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row - 1][guess_col - 1] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row - 1][guess_col - 1] = "X"
        if turn >= 3:
            print("Game Over!! You Lost !!")
            board[ship_row - 1][ship_col - 1] = "*"
            print_board(board)
            print("X = Your Guess(es)")
            print("* = My Battleship")

