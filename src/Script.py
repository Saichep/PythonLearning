#!/usr/bin/env python

from datetime import datetime

from math import sqrt

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
    """Learn about variables"""
    my_int = 7
    my_float = 1.23
    my_bool = True
    print('value of my_int is =', my_int)
    print('value of my_float is =', my_float)
    print('value of my_bool is =', my_bool)
    print('value of my_bool negated is =', not my_bool)


def count_eggs():
    """Learn about return statements"""
    eggs = 12
    return eggs


def biggest_number(*args):
    valid = True
    for arg in args:
        if not isinstance(arg, int):
            valid = False
            break
    if valid:
        return max(args)
    else:
        return "Wrong arguments !!"


def smallest_number(*args):
    valid = True
    for arg in args:
        if not isinstance(arg, int):
            valid = False
            break
    if valid:
        return min(args)
    else:
        return "Wrong arguments !!"


def distance_from_zero(arg):
    if type(arg) == int or type(arg) == float:
        return abs(arg)
    else:
        return "Wrong arguments !!"


def distance_from_zero_again(arg):
    if type(arg) == int or type(arg) == float:
        return abs(arg)
    else:
        return "Wrong arguments !!"


def learn_math_operations():
    """Learn about Mathematical Operations"""
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
    print(x, "square root(using inbuilt function) = ", int(sqrt(25)))
    print("Biggest Number is =", biggest_number(-10, -5, 5, 10))
    print("Smallest Number is =", smallest_number(-10, -5, 5, 10))
    print("Distance between -10 and Zero is =",distance_from_zero(-10))
    print("Distance between 4 and Zero again is =",distance_from_zero_again(4))


def restaurant_bill_calculator(meal_cost: float, tax_percentage: float, tip_percentage: float, currency: str):
    """Calculates the bill including tax and tip"""
    subTotal = meal_cost + meal_cost * (tax_percentage / 100)
    total = subTotal + subTotal * (tip_percentage / 100)
    print("SubTotal with Tax = %.2f" % subTotal, currency)
    print("Total (including tax and tip) = %.2f" % total, currency)


def string_index(string_var: str, index: int):
    """
    The string "PYTHON" has six characters, numbered 0 to 5, as shown below:
    +---+---+---+---+---+---+
    | P | Y | T | H | O | N |
    +---+---+---+---+---+---+
      0   1   2   3   4   5
    So if you wanted "Y", you could just type "PYTHON"[1] (always start counting from 0!)
    """
    if index <= len(string_var):
        print("%d'th char of %s is %s" %(index, string_var,string_var[index]))
    else:
        print("Index out of range: Keep it <= %s" %len(string_var))


def play_with_strings(string_var: str):
    """Playing around with strings"""
    string_index(string_var, len(string_var)-2)
    print("%s in lower case= %s" %(string_var, string_var.lower()))
    print("%s in upper case= %s" %(string_var, string_var.upper()))
    print("Slice[0] of " + string_var + " is = " + string_var[0])
    print("Slice[0:<stringLength>] of " + string_var + " is = " + string_var[0:len(string_var)])


def check_string_isalpha(string_var: str):
    """Checks if a string is not empty and has only alphabetic characters"""
    if len(string_var) > 0 and string_var.isalpha():
        return True
    else:
        return False


def check_isnumeric(numeric_var: str):
    """Checks if a string is not empty and has only numbers"""
    if len(numeric_var) > 0 and numeric_var.isnumeric():
        return True
    else:
        return False


def ask_and_rephrase_about_me():
    """Take user's input based on answers to the questions and infers back the same with validations"""
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
    """Prints date and time in pretty format"""
    now = datetime.now()
    print('Today is %s/%s/%s' % (now.month, now.day, now.year))
    print('Time is %s:%s:%s' % (now.hour, now.minute, now.second))


def greater_less_equal(answer: int, compare_value: int):
    """Checks if the given number is greater, lesser or equal to given number"""
    response = "Dont Know"
    if answer > compare_value:
        response="Yes"
    elif answer < compare_value:
        response="No"
    else:
        response="Both are equal"
    return str(answer) + ">" + str(compare_value) + "==" + response


def arithmetic_and_logical_operators():
    """Test Case for arithmetic and logical operations"""
    if 2 <= 5:
        print("Success #1")

    if True and not False:
        print("Success #2")

    print (greater_less_equal(4,5))
    print (greater_less_equal(5,5))
    print (greater_less_equal(6,5))


def slicing_lists(input_list: list, start_index: int, end_index: int):
    """Slicing of lists"""


def slicing_strings_lists(input_object, start_index: int, end_index: int):
    """Slices a given string or list"""
    if start_index is None:
        start_index = 0
    if end_index is None:
        end_index = len(input_object)
    return input_object[start_index:end_index]


def slicing_test():
    string_test = "catdogfrog"
    print("dog=", slicing_strings_lists(string_test, 3, 6))
    print("cat=", slicing_strings_lists(string_test, None , 3))
    print("frog=", slicing_strings_lists(string_test, 6, None))

    list_items = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
    print(slicing_strings_lists(list_items, 3, 6))
    print(slicing_strings_lists(list_items, None , 3))
    print(slicing_strings_lists(list_items, 4, None))


def finished_concepts():
    """Contains all the concepts that I have finished learning"""
    multi_line_comment()
    print('count of eggs is = %d' %(count_eggs()))
    learn_variables()
    learn_math_operations()
    restaurant_bill_calculator(44.50, 6.75, 15.0, "$")
    play_with_strings("Hello Python!")
    ask_and_rephrase_about_me()
    print_date_and_time_pretty_format()
    slicing_test()


sayHello()
#finished_concepts()


