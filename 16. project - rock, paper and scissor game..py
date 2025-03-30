# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 14:54:29 2025

@author: Dell
"""

#rock, paper and scissors game

import random

game_image = ["rock", "paper", "scissors"]
user_choice = int(input("what do you want to choose? type 0 from rock, 1 for paper and 2 for scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number. you lost!")
    
else:
    print(game_image[user_choice])

    computer_choice = random.randint(0,2) 
    print("computer chose")
    print(game_image[computer_choice])
    
    if user_choice == 0 and computer_choice == 2:
        print("you win!!")
        
    elif computer_choice == 0 and user_choice == 2:
        print("you lost!!")
        
    elif computer_choice > user_choice:
        print("you lost!!")
        
    elif user_choice > computer_choice:
        print("you win!!")
        
    elif computer_choice == user_choice:
        print("it's a draw!!")
        
        