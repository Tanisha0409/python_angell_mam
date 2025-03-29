# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 12:45:19 2025

@author: Dell
"""

# pizza order

'''
small pizza - $ 15
medium pizza -$20
large pizza -$ 25

pepperoni for small pizza = +$2
pepperoni for medium or large pizza = +$3

extra cheese for any pizza is = +$1

input = size = l, add_pepperoni = y, extra_cheese = n
output = your final bill = $28
'''
print("welcome to python pizza delivery!!!")
size = input("what size of pizza do you want to order? s, m, l ")
add_pepperoni = input("do you want pepperoni? y or n ")
extra_cheese = input("do you want extra cheese on pizza? y or n ")

bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
else:
    bill += 25

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == 'y':
    bill += 1

print(f"your final bill for pizza is {bill}.")        