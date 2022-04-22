'''
@Author: Nikita
@Date: 2022-04-20 10: 55: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-20 10:55:00
@Title:Write a Python program to remove item from a tuple.

'''
if __name__=="__main__":
    myTuple=(25,66,9,7,3)
    print("Tuple list is: ",myTuple)
    newList=list(myTuple)
    newList.remove(66)
    myTuple=tuple(newList)
    print("After Removing element from tuple: ",myTuple)