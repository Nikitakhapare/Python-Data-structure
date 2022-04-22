'''
@Author: Nikita
@Date: 2022-04-20 10: 55: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-20 10:55:00
@Title:Write a Python program to Slice a tuple.

'''
if __name__=="__main__":
    myTuple=(25,66,9,7,3,11,45)
    print("Tuple list is: ",myTuple)

    sliceTuple=myTuple[3:6]
    print("After sicing tuple Become: ",sliceTuple)

    sliceTuple=myTuple[::2]
    print("After sicing tuple Become: ",sliceTuple)
