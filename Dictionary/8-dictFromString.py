'''
@Author: Nikita
@Date: 2022-04-21 12:10: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 12:10:00
@Title:Write a Python program to create a dictionary from a string

'''
str = 'w3resource'
my_dict = {}

for i in str:
    my_dict[i] = my_dict.get(i, 0) + 1
    
print("Dictionary is: ",my_dict)