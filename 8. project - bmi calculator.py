# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 11:22:11 2025

@author: Dell
"""

#bmi calculator

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#bmi = weight/height**2 -type error

bmi = int(weight)/float(height)**2
print(int(bmi))