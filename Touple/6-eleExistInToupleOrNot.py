'''
@Author: Nikita
@Date: 2022-04-20 10: 55: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-20 10:55:00
@Title:Write a Python program to check whether an element exists within a tuple.

'''
if __name__=="__main__":
    ele=input("Enter a Element you want to check: ")
    myTouple=("red","green","Orange") 
    if ele in myTouple:
        print("Elemet Exist")
    else:
        print("Element Not Exist.")