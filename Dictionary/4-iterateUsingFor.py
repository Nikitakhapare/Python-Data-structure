'''
@Author: Nikita
@Date: 2022-04-21 05: 10: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 05.10:00
@Title:Write a Python program to iterate over dictionaries using for loops.
'''

my_dict = {1:"red",2:"green",3:"blue",4:"pink"}

#iterate values
for color in my_dict.values():
    print(color, end=" ")

#iterate key and values
print()
for i, color in my_dict.items():
    print( i, ":" , color)

#Gives Key 
for i in my_dict:
    print(i)