#!/usr/bin/env python

__author__ = "Sudheer Veeravalli <veersudhir83@gmail.com>"
__copyright__ = "Copyright (c) 2017. Sudheer Veeravalli. Free for general use and re-distribution"
__license__ = "Public Domain"
__version__ = "1.0"

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3 }

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15 }


def show_stock_vs_price():
    for key in prices:
        print(key, "==>> price: %s stock: %s" %(prices[key],stock[key]))
        # print("price: %s" % prices[key])
        # print("stock: %s" % stock[key])


def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total


show_stock_vs_price()
print("Bill = ", compute_bill(["apple", "banana"]))
show_stock_vs_price()