'''
@Author: Nikita
@Date: 2022-04-21 04: 30: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 04:30:00
@Title:Write a Python script to add a key to a dictionary.

'''

my_dict = {1: 23,2: 67,4: 12,3: 90}
print(my_dict)
my_dict[5]=12
#adding nasted Dictiomary
my_dict[6]=dict({1:'A',2:'B'})
print("After adding key to dictionary: ",my_dict)