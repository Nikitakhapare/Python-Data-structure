'''
@Author: Nikita
@Date: 2022-04-21 12:15: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 12:15:00
@Title:Write a Python script to generate and print a dictionary that contains a 
    number (between 1 and n) in the form (x, x*x)..

'''
my_dict = {}

n = int(input("Enter The Nth Number To Add Values"))

for i in range(1, n):
    my_dict.update({i:i*i})

print("Dictionary  Is: ",my_dict)
