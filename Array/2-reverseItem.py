'''
@Author: Nikita
@Date: 2022-04-21 14: 30: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 14:30:00
@Title:Write a Python program to create array to reverse the item of array.
'''
from array import *

if __name__=="__main__":
    arr=array("i",[1,5,6,8,9])
    print("Array is: ",arr)
    arr.reverse()
    print("elements of array are: ",arr)
    