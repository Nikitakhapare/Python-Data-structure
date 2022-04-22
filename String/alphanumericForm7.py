'''
@Author: Nikita
@Date: 2022-04-18 11: 55: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-18 11:55:00
@Title: Write a Python program that accepts a comma separated sequence of words as input
       and prints the unique words in sorted form (alphanumerically).
'''


string=input("Enter a string ")
list_of_strings = string.split(",")
set_of_string = sorted(set(list_of_strings))

print("Unique string is: ",set_of_string)
