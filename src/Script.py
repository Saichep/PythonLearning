#!/usr/bin/env python

from datetime import datetime
from math import sqrt
import os

from MyStrings import *
from MyMath import *
from jsonio import *

__author__ = "Sudheer Veeravalli <veersudhir83@gmail.com>"
__copyright__ = "Copyright (c) 2017. Sudheer Veeravalli. Free for general use and re-distribution"
__license__ = "Public Domain"
__version__ = "1.0"


def say_hello():
    print('Welcome to Python!')
    print('')


def multi_line_comment():
    """
    multi
    line
    comment"""
    print('processed multi line comment')


def play_with_variables():
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


def play_with_math():
    """Learn about Mathematical Operations"""
    x = 10
    y = 3
    float_val = 0.5
    print(x, "plus", y, "=", x + y)
    print(x, "minus", y, "=", x - y)
    print(x, "multiplied by", float_val, "=", x * float_val)
    print(x, "divided by", y, "=", x / y)
    print(x, "to power of (exponential)", y, "=", x ** y)
    print(x, "modulus", y, "=", x % y)
    print(x, "square root(", float_val, ")=", x ** float_val)
    print(x, "square root(using inbuilt function) = ", int(sqrt(25)))
    print("Biggest Number is =", biggest_number(-10, -5, 5, 10))
    print("Smallest Number is =", smallest_number(-10, -5, 5, 10))
    print("Distance between -10 and Zero is =", distance_from_zero(-10))


def restaurant_bill_calculator(meal_cost: float, tax_percentage: float, tip_percentage: float, currency: str):
    """Calculates the bill including tax and tip"""
    sub_total = meal_cost + meal_cost * (tax_percentage / 100)
    total = sub_total + sub_total * (tip_percentage / 100)
    print("SubTotal with Tax = %.2f" % sub_total, currency)
    print("Total (including tax and tip) = %.2f" % total, currency)


def play_with_strings():
    """Playing around with strings"""
    string_var = "hello python !!"

    string_var = capitalize(string_var, None)
    print("capitalize_string =%s" % string_var)
    ind = 7
    result = chart_at_index(string_var, ind)
    print("%d'th char of %s is %s" % (len(string_var)-8, string_var, result))

    print("\"%s\" in lower case= %s" % (string_var, string_var.lower()))
    print("\"%s\" in upper case= %s" % (string_var, string_var.upper()))

    print("Reversed String(inbuilt) =%s" % (reverse(string_var, None)))
    print("Reversed String(custom) =%s" % (reverse(string_var, False)))

    print("Slice[0] of \"%s\" is =%s" % (string_var, string_var[0]))
    sliced_val = sliced("", 0, None)
    print("Slice[0:%d] of \"%s\" is =%s" %(ind, string_var, sliced_val))

    n = ["Sudheer", "Veeravalli"]

    print(join_with_delimiter(n, None))
    # joins the strings using the delimiter
    print(join_with_delimiter(n, "---"))


def ask_and_rephrase_about_me():
    """Take user's input based on answers to the questions and infers back the same with validations"""
    name = input("What is your name? ")
    quest = input("What is your quest? ")
    color = input("What is your favorite color? ")
    age = input("Your age? ")

    if is_alpha_numeric(name) and is_alpha_numeric(quest) and is_alpha_numeric(color) \
            and is_numeric(age):
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
    if answer > compare_value:
        response = "Yes"
    elif answer < compare_value:
        response = "No"
    else:
        response = "Both are equal"
    return str(answer) + ">" + str(compare_value) + "==" + response


def arithmetic_and_logical_operators():
    """Test Case for arithmetic and logical operations"""
    if 2 <= 5:
        print("Success #1")

    if True and not False:
        print("Success #2")

    print(greater_less_equal(4, 5))
    print(greater_less_equal(5, 5))
    print(greater_less_equal(6, 5))


def slicing_test():
    string_test = "catdogfrog"
    print("dog=", sliced(string_test, 3, 6))
    print("cat=", sliced(string_test, None , 3))
    print("frog=", sliced(string_test, 6, None))

    list_items = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
    print(sliced(list_items, 3, 6))
    print(sliced(list_items, None , 3))
    print(sliced(list_items, 4, None))


def play_with_lists():
    input_list = [5, 3, 1, 2, 4]
    input_list.sort()
    print("Input List = ", input_list)

    def range_operations():
        for i in range(len(input_list)):
            print(input_list[i])

    range_operations()
    squared_list = []
    for number in input_list:
        squared_list.append(number ** 2)
    squared_list.sort()
    print("Squared List = ", squared_list)

    #  pop, remove and del operations
    #  list.pop(index) will remove the item at index from the list and return it to you:
    #  list.remove(item) will remove the actual item if it finds it
    #  del(list[index]) is like .pop in that it will remove the item at the given index, but it won't return it:
    popped_item = input_list.pop(0)
    print("Popped ", popped_item, " from ", input_list)
    input_list.remove(input_list[0])
    print("After remove first element in list", input_list)
    del(input_list[len(input_list)-1])
    print("After del(item at last index)", input_list)

    n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

    #  Add your function here
    def flatten(lists):
        results = []
        for numbers in lists:
            for num in numbers:
                results.append(num)
        return results

    print(flatten(n))

    #  When there's need to iterate over two lists at once. This is where the built-in zip function comes in handy.
    #  zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.
    list_a = [3, 9, 17, 15, 19]
    list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

    for a, b in zip(list_a, list_b):
        # Add your code here!
        if a > b:
            print(a)
        elif b > a:
            print(b)
        else:
            print(a)

    # In this case, the else statement is executed after the for,
    # but only if the for/while loop ends normally —that is, NOT with a break.
    # This code will break when it hits 'tomato', so the else block won't be executed.
    fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

    print('You have...')
    for f in fruits:
        if f == 'tomato':
            print('A tomato is not a fruit!')
            break
        print('A', f),
    else:
        print('A fine selection of fruits!')


def play_with_dictionaries():
    # Assigning a dictionary with three key-value pairs to residents:
    residents = {'Puffin': 104, 'Sloth': 105, 'Burmese Python': 106}
    print(residents['Puffin'])
    print(residents['Sloth'])
    print(residents['Burmese Python'])

    inventory = {'gold': 500, 'pouch': ['flint', 'twine', 'gemstone'],
                 'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf'],
                 'burlap bag': ['apple', 'small ruby', 'three-toed sloth']}

    # Sorting the list found under the key 'pouch'
    inventory['pouch'].sort()

    inventory['pocket'] = ['seashell', 'strange berry', 'lint']
    inventory['backpack'].sort()
    inventory['backpack'].remove('dagger')
    inventory['gold'] += 50
    print(inventory)


def play_with_collections():
    """Looping through various collections"""
    #  lists
    names = ["Adam", "Alex", "Mariah", "Martine", "Columbus"]
    for name in names:
        print(name)

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    even = []
    odd = []
    for val in numbers:
        if val % 2 == 0:
            even.append(val)
        else:
            odd.append(val)
    print("Even Numbers = ", even)
    print("Odd Numbers = ", odd)

    #  dictionary
    webster = {
        "Aardvark": "A star of a popular children's cartoon show.",
        "Baa": "The sound a goat makes.",
        "Carpet": "Goes on the floor.",
        "Dab": "A small amount."
    }
    #  Add your code below!
    for key in webster:
        print(webster[key])

    #  Write your function below!
    def fizz_count(x):
        count = 0
        for item in x:
            if item == "fizz":
                count = count + 1
        return count

    print("Occurrence of \"fizz\" = ", fizz_count(["fizz", "cat", "fizz"]))


def test_my_math():
    print(custom_add(["a"], ["b"]))
    print(custom_add([1, 2, 3], [4, 5, 6], [4, 5, 6]))
    print(custom_add(1, 2))
    print(custom_add(1.5, 2.3))
    print(custom_add(1.5, 2.3, 3.8))


def test_json():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(current_dir, "shares.json")
    print(current_dir)

    print("in test_json() method")
    json_data = {
        'ACME': {
                'name': 'ACME',
                'shares': 100,
                'price': 542.23
            },
        'LAKME': {
                'name': 'LAKME',
                'shares': 200,
                'price': 242.23
            }
        }

    put(json_data, filename)
    json_data_get = get(filename)
    print(json_data_get)
    try:
        if json_data_get["ACME"]["price"]:
            json_data_get["ACME"]["price"] = 1642.23
            print(json_data_get)
            put(json_data_get, filename)
        return 0
    except:
        raise Exception("Can't write data. Verify and re-submit")


def play_with_lambdas():
    languages = ["HTML", "JavaScript", "Python", "Ruby"]
    print(filter(lambda x: x == "Python", languages))

    cubes = [x ** 3 for x in range(1, 11)]
    print(filter(lambda x: x % 3 == 0, cubes))

    garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
    print(garbled[::-1][::2])

    garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
    print(filter(lambda x: x != "X", garbled))


def finished_concepts():
    """Contains all the concepts that I have finished learning"""
    multi_line_comment()
    print('count of eggs is = %d' % (count_eggs()))
    play_with_variables()
    play_with_strings()
    ask_and_rephrase_about_me()
    play_with_math()
    play_with_lists()
    slicing_test()
    play_with_dictionaries()
    play_with_collections()
    print_date_and_time_pretty_format()
    restaurant_bill_calculator(44.50, 6.75, 15.0, "$")
    test_my_math()
    print(sliced.__doc__)
    print(remove_duplicates(["hey", "buddy", "hey"]))
    print(median([4, 5, 5, 4]))
    play_with_lambdas()


my_str = 'TestSlicingInPython'

print(my_str[my_str.index("test".capitalize()):my_str.index("slicing".capitalize())])
print(my_str[my_str.index("slicing".capitalize()):my_str.index("in".capitalize())])
print(my_str[my_str.index("in".capitalize()):my_str.index("python".capitalize())])
print(my_str[my_str.index("python".capitalize()):])

say_hello()
# finished_concepts()
inp = 12
n = 0
mask = n << 2
result = inp ^ n
result2 = inp ^ mask
print(bin(result))
print(bin(result2))
