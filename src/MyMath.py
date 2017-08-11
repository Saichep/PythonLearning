#!/usr/bin/env python

__author__ = "Sudheer Veeravalli <veersudhir83@gmail.com>"
__copyright__ = "Copyright (c) 2017. Sudheer Veeravalli. Free for general use and re-distribution"
__license__ = "Public Domain"
__version__ = "1.0"


def is_int(x: int):
    """returns True if a number is a true integer; False otherwise"""
    if x - round(x) == 0:  # If Difference between he number and it's rounded value is Zero, then it's a true integer
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
    """
    Returns factorial value for given number
    :param x:int
    :return: Object
    """
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


def biggest_number(*args):
    """
    Returns the biggest number in a given list of integers
    :param args:list
    :return: Object
    """
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
    """
    Returns the smallest number in a given list of integers
    :param args: list
    :return: Object
    """
    valid = True
    for arg in args:
        if not isinstance(arg, int):
            valid = False
            break
    if valid:
        return min(args)
    else:
        return None


def validate_collections(*args):
    """
    Returns True if the parameters are all of the same type. Else returns False
    :param args: list
    :return: boolean
    """
    valid = False
    for index in range(1,len(args)):
        if type(args[0]) == type(args[index]):
            valid = True
        else:
            valid = False
            break
    return valid


def custom_add(*args):
    """
    Adds/appends the two or more objects/collections into a single one
    :param args: Collection of objects
    :return: Object
    Usage:
        custom_add(["a"], ["b"]); custom_add([1, 2, 3], [4, 5, 6], [4, 5, 6])
        custom_add(1, 2);  custom_add(1.5, 2.3);  custom_add(1.5, 2.3, 3.8)
    """
    result = None
    if validate_collections(*args):
        if isinstance(args[0], int) or isinstance(args[0], float):
            result = sum(args)
        elif isinstance(args[0], list):
            result = []
            for list_object in args:
                for item in list_object:
                    result.append(item)
        else:
            raise Exception('Exception in custom_add: The data type of the provided arguments is not implemented')
    else:
        raise Exception('Exception in custom_add: The data type of the provided arguments is not the same')
    return result


def custom_subtract(*args):
    """
    Subtracts/removes the two or more objects/collections into a single one
    :param args: Collection of objects
    :return: Object
    Usage:
        custom_subtract(["a"], ["b"]);  custom_subtract([1, 2, 3], [4, 5, 6], [4, 5, 6])
        custom_subtract(1, 2);  custom_subtract(1.5, 2.3);   custom_subtract(1.5, 2.3, 3.8)
    """
    result = None
    if validate_collections(*args):
        if isinstance(args[0], int) or isinstance(args[0], float):
            result = args[0]
            for index in range(1,len(args)):
                result -= args[index]
        else:
            raise Exception('Exception in custom_subtract: The data type of the provided arguments is not implemented')
    else:
        raise Exception('Exception in custom_subtract: The data type of the provided arguments is not the same')
    return result

