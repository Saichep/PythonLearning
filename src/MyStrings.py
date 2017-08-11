#!/usr/bin/env python

__author__ = "Sudheer Veeravalli <veersudhir83@gmail.com>"
__copyright__ = "Copyright (c) 2017. Sudheer Veeravalli. Free for general use and re-distribution"
__license__ = "Public Domain"
__version__ = "1.0"


def isalphanumeric(x: str) -> bool:
    """
    Checks if a string is not empty and has only alphabetic characters
    :param x: str
    :return: bool
    """
    if len(x) > 0 and x.isalpha():
        return True
    else:
        return False


def isnumeric(x: str) -> bool:
    """
    Checks if a string is not empty and has only numbers
    :param x: str
    :return: bool
    """
    if len(x) > 0 and x.isnumeric():
        return True
    else:
        return False


def capitalize(x: str, delimiter: str) -> str:
    """
    Returns the camel notation for all the words in the given string.
    The default .capitalize() function in 'str' module only camel's the first word of the string.
    So, converted all the words in the given string into list of words, capitalized each and returned.
    Delimited may be passed, but default is space " "
    :param x: str
    :param delimiter: str
    :return: str
    """
    if delimiter is None or len(delimiter) == 0:
        delimiter = " "
    sub_strings = x.split(" ")
    for index in range(len(sub_strings)):
        sub_strings[index] = sub_strings[index].capitalize()
    return delimiter.join(sub_strings)


def chart_at_index(string_var: str, index: int) -> str:
    """
    Returns the character at the given index of the string_var
    :param string_var: str
    :param index: int
    :return: str
    """
    if index < len(string_var):
        return string_var[index]
    else:
        raise Exception("Exception in MyStrings.index(): Index out of range")


def reverse(x: str, use_inbuilt: bool) -> str:
    """
    Returns the reversed value of given string.
        If use_inbuilt is True = In-built function will be used;
        Else, my custom version will be used
    :param x: str
    :param use_inbuilt: bool
    :return: str
    """
    result = ""
    if use_inbuilt is None:
        use_inbuilt = True

    if use_inbuilt:
        result = x[::-1]
    else:
        index = len(x) - 1
        while index >= 0:
            result += x[index]
            index -= 1
    return result


def sliced(x: str, start_index: int, end_index: int) -> str:
    """
    Returns the sliced portion of given string.
        If use_inbuilt is True = In-built function will be used;
        Else, my custom version will be used
    :param x: str
    :param start_index: int
    :param end_index: int
    :return: str
    """
    if x is None:
        raise Exception("Exception in MyStrings.sliced(): Input String is Null / None")
    if start_index is None:
        start_index = 0
    if end_index is None:
        end_index = len(x)
    return x[start_index: end_index]


def join_with_delimiter(x: str, delimiter: str) -> str:
    """
    Returns the sliced portion of given string.
        If use_inbuilt is True = In-built function will be used;
        Else, my custom version will be used
    :param x: str
    :param delimiter: str
    :return: str
    """
    if delimiter is None or delimiter in ["",'']:
        delimiter = " "
    return delimiter.join(x)