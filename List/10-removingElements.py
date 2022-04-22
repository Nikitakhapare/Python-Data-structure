'''
@Author: Nikita
@Date: 2022-04-19 16: 30: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 16:30:00
@Title:Write a Python program to remove Element at specific location
'''
my_list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del my_list[4:6]
my_list.pop(0)
print("list after removing element at given location: ",my_list)