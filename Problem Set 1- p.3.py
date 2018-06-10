# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:52:03 2018

@author: jillhkm
"""

# getting inital inputs
balance = float(input("Inital balance at beginning of the year: "))
annualInterestRate = float(input("What is the yearly interst rate? "))


monthlyir = float(annualInterestRate / 12)

# calculating upper and lower
upperbound = (balance * ((1 + monthlyir)**12)) / 12
lowerbound = (balance / 12)

# first payment
p = ((upperbound + lowerbound) / 2)


def testbal(balance, p):
    """
    tests to see if payment will work as minimum
    """
    # month 1 - 12
    i = 1
    ub = balance - p
    while i < 12:
        ub = ((ub + (monthlyir * ub)) - p)
        i += 1
    return ub


ub = round(testbal(balance, p), 2)

while ub != 0.00:
    if ub > 0.00:
        upperbound = upperbound
        lowerbound = p
        p = ((upperbound + lowerbound) / 2)
        ub = round(testbal(balance, p), 2)
    else:
        upperbound = p
        lowerbound = lowerbound
        p = ((upperbound + lowerbound) / 2)
        ub = round(testbal(balance, p), 2)

print("Lowest Payment: ", round(p, 2))
