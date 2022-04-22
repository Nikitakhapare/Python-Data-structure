'''
@Author: Nikita
@Date: 2022-04-18 08: 20: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-18 08:20:00
@Title: Write a Python program to count the number of characters (character frequency) in a
string
'''


string="google.com"
str=(list(string))
print(str)
dict_of_count={item:str.count(item) for item in str}
print("Number of Characters are: ",dict_of_count)