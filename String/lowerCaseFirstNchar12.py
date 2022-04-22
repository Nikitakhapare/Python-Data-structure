'''
@Author: Nikita
@Date: 2022-04-18 11: 45: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-18 12:45:00
@Title:Write a Python program to lowercase first n characters in a string
one.
'''


string=input("Enter a string")
n=int(input("Enter how many character you want in lower case. "))
print("String Become: ",string[:n].lower()+string[n:])

