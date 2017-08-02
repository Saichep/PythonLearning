#!/usr/bin/env python

__author__ = "Sudheer Veeravalli <veersudhir83@gmail.com>"
__copyright__ = "Copyright (c) 2017. Sudheer Veeravalli. Free for general use and re-distribution"
__license__ = "Public Domain"
__version__ = "1.0"

def sayHello():
    print('Welcome to Python!')

def multiLineComment():
    """
    multi
    line
    comment"""
    print('processed multi line comment')

def learnVariables():
    my_int = 7
    my_float = 1.23
    my_bool = True
    print('value of my_int is =', my_int)
    print('value of my_float is =', my_float)
    print('value of my_bool is =', my_bool)
    print('value of my_bool negated is =', not my_bool)

# Indentation
def countEggs():
    eggs = 12
    return eggs

# math operations
def learnMathOperations():
    x = 10
    y = 3
    float = 0.5
    print(x, "plus", y, "=", x + y)
    print(x, "minus", y, "=", x - y)
    print(x, "multiplied by", y, "=", x * float)
    print(x, "divided by", y, "=", x / y)
    print(x, "to power of (exponential)", y, "=", x ** y)
    print(x, "modulus", y, "=", x % y)

def restaurantBillCalculator(mealCost, tax_percentage, tip_percentage, currency):
    subTotal = mealCost + mealCost * (tax_percentage / 100)
    total = subTotal + subTotal * (tip_percentage / 100)
    print("SubTotal with Tax = %.2f" % subTotal, currency)
    print("Total (including tax and tip) = %.2f" % total, currency)

def stringIndex(stringVar, index):
    """
    The string "PYTHON" has six characters, numbered 0 to 5, as shown below:
    +---+---+---+---+---+---+
    | P | Y | T | H | O | N |
    +---+---+---+---+---+---+
      0   1   2   3   4   5
    So if you wanted "Y", you could just type "PYTHON"[1] (always start counting from 0!)
    """
    if index <= len(stringVar):
        print(index, '\'th char of ',stringVar, 'is', stringVar[index-1])
    else:
        print("Index out of range: Keep it <=", len(stringVar))

def finishedConcepts():
    multiLineComment()
    print('count of eggs is =',countEggs())
    learnVariables()
    learnMathOperations()
    restaurantBillCalculator(44.50, 6.75, 15.0, "$")

sayHello()
stringIndex("Python", 7)