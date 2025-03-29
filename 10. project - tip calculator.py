# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 11:35:37 2025

@author: Dell
"""

#bill splitting with tip
'''
if the bill was $150.0, split between 5 people, with 12% tip
each person should pay (150.0/5)*1.12
round the result to 2 decimal places = 33.60
'''

print("welcome to the tip calculator")

bill = float(input("what was the total bill? $ "))
tip = int(input("how much tip would you like to give? 10, 12, or 15? "))
people = int(input("how many people to split the bill? "))

bill_with_tip = tip/100*bill + bill
print(bill_with_tip)
