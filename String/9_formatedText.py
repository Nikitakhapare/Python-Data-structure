'''
@Author: Nikita
@Date: 2022-04-18 11: 30: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-18 11:30:00
@Title:Write a Python program to display formatted text (width=50) as output

'''


import textwrap

value =input("Enter the paraghraph: ")

# Wrap this text.
string = textwrap.fill(text=value, width=50)
print (string)
