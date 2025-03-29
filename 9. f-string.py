# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 11:26:44 2025

@author: Dell
"""

# f- string

score = 0
height = 1.8
is_winning = True

print(f"your score is {score}, your height is {height}, you are winning is {is_winning}")



#remaining age calculation

age = int(input("enter your current age: "))

years_remaining = 90 - age
months_remaining = years_remaining*12
weeks_remaining = years_remaining*52
days_remaining = years_remaining*365

message = f"you have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left."
print(message)