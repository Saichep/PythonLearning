#!/usr/bin/env python

__author__ = "Sudheer Veeravalli <veersudhir83@gmail.com>"
__copyright__ = "Copyright (c) 2017. Sudheer Veeravalli. Free for general use and re-distribution"
__license__ = "Public Domain"
__version__ = "1.0"


def is_int(x: int):
    """returns True if a number is a true integer; False otherwise"""
    if x - round(x) == 0: # If Difference between he number and it's rounded value is Zero, then it's a true integer
        return True
    else:
        return False


def sum_of_digits(x: int):
    """returns the sum of all numbers in a given integer; if less than zero, it will return zero"""
    result = 0
    if x >= 0:
        for digit in str(x):
            result += int(digit)
    return result


def is_prime(x: int):
    """returns True if the given number is prime number; False otherwise"""
    result = True
    if x <= 1:
        result = False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                result = False
    return result


def factorial(x):
    """returns factorial value for given number"""
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


def biggest_number(*args):
    """returns the biggest number in a given list of integers"""
    valid = True
    for arg in args:
        if not isinstance(arg, int):
            valid = False
            break
    if valid:
        return max(args)
    else:
        return None


def smallest_number(*args):
    """returns the smallest number in a given list of integers"""
    valid = True
    for arg in args:
        if not isinstance(arg, int):
            valid = False
            break
    if valid:
        return min(args)
    else:
        return None


def custom_add(*args):
    """Adds/appends/concatenates the two or more objects/collections into a single one"""
    result = 0;
    if isinstance(args[0], int):
        result = int(0)
        for item in args:
            result += item
    elif isinstance(args[0], float):
        result = float(0)
        for item in args:
            result += item
    elif isinstance(args[0], str):
        result = ""
        for item in args:
            result += item
    elif isinstance(args[0], list):
        result = []
        for list_object in args:
            for item in list_object:
                result.append(item)
    else:
        result = None

    return result
