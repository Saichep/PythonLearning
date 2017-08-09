#!/usr/bin/env python

__author__ = "Sudheer Veeravalli <veersudhir83@gmail.com>"
__copyright__ = "Copyright (c) 2017. Sudheer Veeravalli. Free for general use and re-distribution"
__license__ = "Public Domain"
__version__ = "1.0"

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]


def print_all_students():
    for student in students:
        print(student["name"])
        print(student["homework"])
        print(student["quizzes"])
        print(student["tests"])


def average(numbers):
    average_val = float(sum(numbers)/len(numbers))
    return average_val


def get_weighted_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    homework *= 0.1
    quizzes *= 0.3
    tests *= 0.6
    total = round(homework + quizzes + tests, 2)
    return total


def get_letter_grade(score: int):
    if score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"


def get_class_average(class_list):
    results = []
    for student in class_list:
        results.append(get_weighted_average(student))
    return average(results)


for student in students:
    print("Weighted Average of %6s is %4.2f" %(student["name"], get_weighted_average(student)))
    print("Grade is %s" % get_letter_grade(int(get_weighted_average(student))))

print("Class Average = ", round(get_class_average(students),2))
print("Class Average Grade = ",get_letter_grade(get_class_average(students)))