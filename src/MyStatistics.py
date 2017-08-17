#!/usr/bin/env python

__author__ = "Sudheer Veeravalli <veersudhir83@gmail.com>"
__copyright__ = "Copyright (c) 2017. Sudheer Veeravalli. Free for general use and re-distribution"
__license__ = "Public Domain"
__version__ = "1.0"

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def sum_grades(scores: list) -> float:
    """
    Returns the sum of given grades
    :param scores: list
    :return: float
    """
    total = 0
    for score in scores:
        total += score
    return total


def average_grades(scores: list) -> float:
    """
    Returns the average of given grades
    :param scores: list
    :return: float
    """
    sum_of_grades = sum(scores)
    average = sum_of_grades / float(len(scores))
    return average


def variance_grades(scores: list) -> float:
    """
    Returns the variance of given grades
    :param scores: list
    :return: float
    """
    average = average_grades(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / float(len(scores))


def std_deviation_grades(scores: list) -> float:
    """
    Returns the standard deviation of given grades
    :param scores: list
    :return: float
    """
    return variance_grades(scores) ** 0.5
