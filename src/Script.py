#!/usr/bin/env python

from datetime import datetime

__author__ = "Sudheer Veeravalli <veersudhir83@gmail.com>"
__copyright__ = "Copyright (c) 2017. Sudheer Veeravalli. Free for general use and re-distribution"
__license__ = "Public Domain"
__version__ = "1.0"


def sayHello():
    print('Welcome to Python!')


def multi_line_comment():
    """
    multi
    line
    comment"""
    print('processed multi line comment')


def learn_variables():
    my_int = 7
    my_float = 1.23
    my_bool = True
    print('value of my_int is =', my_int)
    print('value of my_float is =', my_float)
    print('value of my_bool is =', my_bool)
    print('value of my_bool negated is =', not my_bool)


# Indentation
def count_eggs():
    eggs = 12
    return eggs


# math operations
def learn_math_operations():
    x = 10
    y = 3
    float = 0.5
    print(x, "plus", y, "=", x + y)
    print(x, "minus", y, "=", x - y)
    print(x, "multiplied by", float, "=", x * float)
    print(x, "divided by", y, "=", x / y)
    print(x, "to power of (exponential)", y, "=", x ** y)
    print(x, "modulus", y, "=", x % y)
    print(x, "square root(", float, ")=", x ** float)


def restaurant_bill_calculator(meal_cost, tax_percentage, tip_percentage, currency):
    subTotal = meal_cost + meal_cost * (tax_percentage / 100)
    total = subTotal + subTotal * (tip_percentage / 100)
    print("SubTotal with Tax = %.2f" % subTotal, currency)
    print("Total (including tax and tip) = %.2f" % total, currency)


def string_index(string_var, index):
    """
    The string "PYTHON" has six characters, numbered 0 to 5, as shown below:
    +---+---+---+---+---+---+
    | P | Y | T | H | O | N |
    +---+---+---+---+---+---+
      0   1   2   3   4   5
    So if you wanted "Y", you could just type "PYTHON"[1] (always start counting from 0!)
    """
    if index <= len(string_var):
        print("%d'th char of %s is %s" %(index, string_var,string_var[index - 1]))
    else:
        print("Index out of range: Keep it <= %s" %len(string_var))


def play_with_strings(string_var):
    string_index(string_var, 7)
    print("%s in lower case= %s" %(string_var, string_var.lower()))
    print("%s in upper case= %s" %(string_var, string_var.upper()))


def check_string_isalpha(string_var):
    # checks if a string is not empty and has only alphabetic characters
    if len(string_var) > 0 and string_var.isalpha():
        return True
    else:
        return False

def check_isnumeric(numeric_var):
    # checks if a string is not empty and has only alphabetic characters
    if len(numeric_var) > 0 and numeric_var.isnumeric():
        return True
    else:
        return False

def ask_and_rephrase_about_me():
    name = input("What is your name? ")
    quest = input("What is your quest? ")
    color = input("What is your favorite color? ")
    age = input("Your age? ")

    if check_string_isalpha(name) and check_string_isalpha(quest) and check_string_isalpha(color) \
            and check_isnumeric(age):
        print("Ah, so your name is %s, your quest is %s, your favorite color is %s and your age is %s."
              % (name, quest, color, age))
    else:
        print("Some Inputs are not provided in correct format. Please try again !!")

def print_date_and_time_pretty_format():
    now = datetime.now()
    print('Today is %s/%s/%s' % (now.month, now.day, now.year))
    print('Time is %s:%s:%s' % (now.hour, now.minute, now.second))


def greater_less_equal_5(answer):
    # Switch Statement
    response = "Dont Know"
    if answer > 5:
        response="Yes"
    elif answer < 5:
        response="No"
    else:
        response="Both are equal"
    return str(answer) + ">" + str(5) + "==" + response


def arithmetic_and_logical_operators():
    # Operator preference of evaluation: not, and, or
    if 2 <= 5:
        print("Success #1")

    if True and not False:
        print("Success #2")

    print (greater_less_equal_5(4))
    print (greater_less_equal_5(5))
    print (greater_less_equal_5(6))


def finished_concepts():
    multi_line_comment()
    print('count of eggs is = %d' %(count_eggs()))
    learn_variables()
    learn_math_operations()
    restaurant_bill_calculator(44.50, 6.75, 15.0, "$")
    play_with_strings("Hello Python!")
    ask_and_rephrase_about_me()
    print_date_and_time_pretty_format()

sayHello()
#finished_concepts()

