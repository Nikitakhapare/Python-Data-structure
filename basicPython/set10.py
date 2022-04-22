'''
@Author: Nikita
@Date: 2022-04-018 12: 27: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-18 12:27:00
@Title: Write a Python program to print out a set containing all the colors from
color_list_1 which are not present in color_list_2. 
'''


color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1-color_list_2)

