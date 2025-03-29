# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 11:43:08 2025

@author: Dell
"""

#conditionals

print("welcome to the rollercoaster! ")

height = int(input("enter your height in cm: "))

if height > 120:
    print("you can ride the rollercoaster!!")
else:
    print("sorry! you have to grow taller before you can ride") 
    
'''    
comparision operator

operator- meaning

1. > - greater than
2. < - smaller tham
3. >= - greater than equal too
4. <= - smaller than equal too
5. == - equal too
6. != - not equal too
'''

#odd/ even

number = int(input("enter any number: "))
if number % 2 == 0:
    print("even number ", number)
else: 
    print("odd number ", number)    
    
    
    

#rollercoaster ride
print("welcome to the rollercoaster!")

height = int(input("enter your height in cm: "))

if height > 120:
    print("you can ride the rollercoaster!")
    age = int(input("enter your age: "))
    # with two possibilities
    if age <= 18:
        print("please pay $ 7")
    else:
        print("please pay $12")
else:
    print("sorry, you have to grow taller to ride ")  
    
    

#rollercoaster ride
print("welcome to the rollercoaster!")

height = int(input("enter your height in cm: "))

if height > 120:
    print("you can ride the rollercoaster!")
    age = int(input("enter your age: "))
    # with three possibilities
    if age <= 12:
        print("please pay $ 5")
    elif age <=18:
        print("please pay $7")
    else:
        print("please pay $12")
else:
    print("sorry, you have to grow taller to ride ")       
    
    
#leap year or not

year = int(input("which year do you want to check? "))    

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
          print("leap year ", year)
        else:
          print("not leap year", year)
    else:
        print("leap year", year)        
else:
    print("not leap year", year)        