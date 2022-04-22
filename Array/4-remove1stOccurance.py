'''
@Author: Nikita
@Date: 2022-04-21 14: 30: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 14:30:00
@Title:Write a Python program to remove the first Occurance of specified element in an array.
'''
from array import *


if __name__=="__main__":
    arr=array("i",[1,5,4,1,8,9])
    print("Array is: ",arr)
    arr.remove(1)
    print("array is: ",arr)

