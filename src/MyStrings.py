#!/usr/bin/env python

__author__ = "Sudheer Veeravalli <veersudhir83@gmail.com>"
__copyright__ = "Copyright (c) 2017. Sudheer Veeravalli. Free for general use and re-distribution"
__license__ = "Public Domain"
__version__ = "1.0"


def is_alpha_numeric(x: str) -> bool:
    """
    Checks if a string is not empty and has only alphabetic characters
    :param x: str
    :return: bool
    """
    if len(x) > 0 and x.isalpha():
        return True
    else:
        return False


def is_numeric(x: str) -> bool:
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


def anti_vowel(x: str) -> str:
    """
    Returns the same string but with vowels (a,e,i,o,u) removed.
    :param x: str
    :return: str
    """
    result = ""
    for char in x:
        if str(char).lower() not in ['a', 'e', 'i', 'o', 'u']:
            result += str(char)
    return result


def scrabble_score(x: str) -> int:
    """
    Scrabble is a game where players get points by spelling words.
    Words are scored by adding together the point values of each individual letter; ignore the case of characters
    :param x: str
    :return: int
    """
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
    result = 0
    for char in x:
        if str(char).lower() in score.keys():
            result += score[str(char).lower()]
        else:
            result += 0
    return result


def censor_text(x: str, censor_string: str) -> str:
    """
    This function returns the given text back but censor's the word with asterisk.
    :param x: str
    :param censor_string: str
    :return: str
    """
    result = ""
    replace_string = ""
    for i in range(0,len(censor_string)):
        replace_string += "*"
    words = x.split()
    for word in words:
        if len(result) > 0:
            result += " "
        if word == censor_string:
            result += " " + replace_string
        else:
            result += " " + word
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
    if delimiter is None or delimiter in ["", '']:
        delimiter = " "
    return delimiter.join(x)


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