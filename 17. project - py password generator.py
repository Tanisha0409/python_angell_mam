# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 15:05:33 2025

@author: Dell
"""

#py password generator

import random

letters = ['a', 'b','c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*','+','_','(',')']

print('welcome to the py-password generator!!')
nr_letters = int(input("how many letters do you want in your password?\n"))
nr_numbers = int(input("how many numbers do you want in your password?\n"))
nr_symbol = int(input("how many symbols do you want in your password?\n"))

#easy level
password = ''
for char in range (1,nr_letters +1):
    password += random.choice(letters)
    
for char in range (1,nr_numbers +1):
    password += random.choice(numbers)

for char in range (1,nr_symbol +1):
    password += random.choice(symbols)    
    
print(password)



#hard level
password_list = []
for char in range (1,nr_letters +1):
    password_list += random.choice(letters)
    
for char in range (1,nr_numbers +1):
    password_list += random.choice(numbers)

for char in range (1,nr_symbol +1):
    password_list += random.choice(symbols)    
    
print(password_list)

random.shuffle(password_list)
print(password_list)

password = ''
for char in password_list:
    password += char
print(f"your password is: {password}")
    