# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 14:35:29 2025

@author: Dell
"""

# treasure island

print("welcome to treasure island")
print("your mission is to find the treasure.")
choice1 = input("you're at a crossroad, where do you want to go? type 'left' or 'right'.\n").lower()

if choice1 == "right":
    choice2 = input("you've come to a lake. there is an island in the middle of the lake. type 'wait' to wait for at boat , or type 'swim'to swim across.\n" ).lower()
    
    if choice2 == 'wait':
        choice3 = input("you arrive at the island unharmed. there is a house with three doors. one red, one yellow and one blue. which colur do you choose? \n").lower()
        
        if choice3 == 'red':
            print("it's a room full of fire. game over!")
            
        elif choice3 == 'yellow':
            print("you found the treasure. you win!")
         
        else:
            print("you entered the room of beasts. game over!")
    else:
        print("you got attacked by an angry trout. game over!")

else:
   print("you fell into a hole. game over!")
         
            
                 