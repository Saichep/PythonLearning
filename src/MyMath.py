#!/usr/bin/env python

__author__ = "Sudheer Veeravalli <veersudhir83@gmail.com>"
__copyright__ = "Copyright (c) 2017. Sudheer Veeravalli. Free for general use and re-distribution"
__license__ = "Public Domain"
__version__ = "1.0"


def is_int(x: int) -> bool:
    """
    Returns True if a number is a true integer; False otherwise
    :param x: int
    :return: bool
    """
    if x - round(x) == 0:  # If Difference between he number and it's rounded value is Zero, then it's a true integer
        return True
    else:
        return False


def sum_of_digits(x: int) -> int:
    """
    Returns the sum of all numbers in a given integer; if less than zero, it will return zero
    :param x: int
    :return: int
    """
    result = 0
    if x >= 0:
        for digit in str(x):
            result += int(digit)
    return result


def is_prime(x: int) -> bool:
    """
    Returns True if the given number is prime number; False otherwise
    :param x: int
    :return: bool
    """
    result = True
    if x <= 1:
        result = False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                result = False
    return result


def factorial(x: int) -> int:
    """
    Returns factorial value for given number
    :param x: int
    :return: int
    """
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


def biggest_number(*args) -> int:
    """
    Returns the biggest number in a given list of integers
    :param args: list
    :return: int
    """
    valid = True
    for arg in args:
        if not isinstance(arg, int):
            valid = False
            break
    if valid:
        return max(args)
    else:
        raise Exception('Exception in MyMath.biggest_number(): The data type of the arguments is not unique.')


def smallest_number(*args) -> int:
    """
    Returns the smallest number in a given list of integers
    :param args: list
    :return: int
    """
    valid = True
    for arg in args:
        if not isinstance(arg, int):
            valid = False
            break
    if valid:
        return min(args)
    else:
        raise Exception('Exception in MyMath.smallest_number(): The data type of the arguments is not unique.')


def distance_from_zero(arg) -> int:
    """
    Returns the distance from Zero
    :param arg: int/float
    :return: int int
    """
    if type(arg) == int or type(arg) == float:
        return abs(arg)
    else:
        raise Exception('Exception in MyMath.distance_from_zero(): The data type of the argument(s) is not supported.')


def validate_collections(*args) -> bool:
    """
    Returns True if the parameters are all of the same type. Else returns False
    :param args: list
    :return: bool
    """
    valid = False
    for index in range(1, len(args)):
        if isinstance(args[index], type(args[0])):
            valid = True
        else:
            valid = False
            break
    return valid


def custom_add(*args) -> object:
    """
    Adds/appends the two or more objects/collections into a single one
    :param args: Collection of objects
    :return: object
    Usage:
        custom_add(["a"], ["b"]); custom_add([1, 2, 3], [4, 5, 6], [4, 5, 6])
        custom_add(1, 2);  custom_add(1.5, 2.3);  custom_add(1.5, 2.3, 3.8)
    """
    if validate_collections(*args):
        if isinstance(args[0], int) or isinstance(args[0], float):
            result = sum(args)
        elif isinstance(args[0], list):
            result = []
            for list_object in args:
                for item in list_object:
                    result.append(item)
        else:
            raise Exception('Exception in MyMath.custom_add(): The data type of the arguments is not implemented.')
    else:
        raise Exception('Exception in MyMath.custom_add(): The data type of the arguments is not the same.')
    return result


def custom_subtract(*args) -> object:
    """
    Subtracts/removes the two or more objects/collections into a single one
    :param args: Collection of objects
    :return: object
    Usage:
        custom_subtract(["a"], ["b"]);  custom_subtract([1, 2, 3], [4, 5, 6], [4, 5, 6])
        custom_subtract(1, 2);  custom_subtract(1.5, 2.3);   custom_subtract(1.5, 2.3, 3.8)
    """
    if validate_collections(*args):
        if isinstance(args[0], int) or isinstance(args[0], float):
            result = args[0]
            for index in range(1, len(args)):
                result -= args[index]
        else:
            raise Exception('Exception in MyMath.custom_subtract(): The data type of the arguments is not implemented.')
    else:
        raise Exception('Exception in MyMath.custom_subtract(): The data type of the arguments is not the same.')
    return result


def count_occurrences(x: list, num: int)-> int:
    """
    Returns the count of occurrences of num in list
    :param x: list
    :param num: int
    :return: int
    """
    result = 0
    for i in x:
        if i == num:
            result += 1
    return result