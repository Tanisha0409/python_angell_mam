# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 22:36:51 2025

@author: Dell
"""

#data type
#string
print("123" + "345")

#integer
print(123 + 345)

#float
print(12.0 + 45.6)

#boolean
print(True + True)
print(True + False)
print(False + True)
print(False + False)


#len(4566)  - error because int have no len

num_char = len(input("what is your name? "))
#print("your name has "+ num_char + "characters") -error str and int can't concat

new_num_char = str(num_char)
print("your name has "+ new_num_char + " characters")



#data type casting
a = 123
print(type(a))

b = "24176"
print(type(b))


c = True
print(type(c))


d = 56.0
print(type(d))



e = str(a)
print(e)


f = float(a)
print(f)


print(70 + float("100.5"))

print(str(70) + str(100))