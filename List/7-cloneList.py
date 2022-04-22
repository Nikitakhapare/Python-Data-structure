'''
@Author: Nikita
@Date: 2022-04-19 15: 55: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 15:55:00
@Title:Write a Python program to clone a list
'''
if __name__=="__main__":
    my_list=[]
    n=int(input("Enter Number of element in list: "))
    for i in range(0,n):
        my_list.append(int(input()))

    new_list=my_list
    print("Original List is: ",my_list)
    print("Copy list is : ",new_list)