# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 12:34:35 2025

@author: Dell
"""

# rollercoaster bill calculation

print("welcome to rollercoster bill calculation! ")
height = int(input("enter your height in cm: "))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster!!")
    age = int(input("enter your age: "))
    if age <= 12:
        bill = 5
        print("child tickets are for $5")
    elif age <= 18:
        bill = 7
        print("youth ticket is for $7")
    else:
        bill = 12
        print("adult ticket if for $12")

want_photo = input("do you want photos to be taken? y or n ") 

if want_photo == "y"       :
    bill += 3
    
print(f"your final bill is {bill}")