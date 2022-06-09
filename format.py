#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: June 2022
# This program uses a function by reference

import math


def rounder(someVariable, amount):
    # function adds 1, by reference

    ten_times = 10**amount
    someVariable[0] = someVariable[0] * ten_times
    someVariable[0] = someVariable[0] + 0.5
    someVariable[0] = int(someVariable[0])
    someVariable[0] = someVariable[0] / ten_times


def main():
    # this function gets a number and calls the add_one function

    someNumber = []
    # input
    number_round = float(input("Enter a number to round: "))
    amount_round = int(input("Enter how many decimal places to round by: "))
    someNumber.append(number_round)
    rounder(someNumber, amount_round)
    print("\nThe rounded number is: {0}".format(someNumber[0]))


if __name__ == "__main__":
    main()
