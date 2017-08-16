#!/usr/bin/env python

__author__ = "Sudheer Veeravalli <veersudhir83@gmail.com>"
__copyright__ = "Copyright (c) 2017. Sudheer Veeravalli. Free for general use and re-distribution"
__license__ = "Public Domain"
__version__ = "1.0"

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def sum_grades(scores):
    total = 0
    for score in scores:
        total += score
    return total


def average_grades(grades_input):
    sum_of_grades = sum(grades_input)
    average = sum_of_grades / float(len(grades_input))
    return average


def variance_grades(scores):
    average = average_grades(scores)
    variance = 0
    for score in scores:
        variance += ( average - score ) ** 2
    return variance / float(len(scores))


def std_deviation_grades(variance):
    return variance ** 0.5
