'''
@Author: Nikita
@Date: 2022-04-21 11: 45: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 11:45:00
@Title:Write a Python program to check multiple keys exists in a dictionary.

'''

my_dict = {1:"red",2:"green",3:"blue",4:"pink"}
 
 #checking all keys exist in dictionary
 
if all(key in my_dict for key in my_dict): 
    print("given all keys are present in dictionary") 
else: 
    print("given all keys are not present in dictionary") 