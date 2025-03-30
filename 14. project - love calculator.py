# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 14:22:13 2025

@author: Dell
"""

#love calculator
'''
input - name1 = "kanye west", name2 = "kim kardashian"
output - your score is 42, you are alright together
'''

print("welcome to the love calculator")
name_1 = input("enter the your name?\n")
name_2 = input("enter their name?\n")

combined_string = name_1 + name_2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t+r+u+e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l+o+v+e

love_score = int(str(true)+str(love))


if (love_score < 10) or (love_score > 90):
    print(f"your love score is {love_score}, you go together like coke and mentos")
    
elif (love_score >= 40) or (love_score <= 50):
    print(f"your love score is {love_score}, you are alright together")
    
else:
    print(f"your love score is {love_score}.")    