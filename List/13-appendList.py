'''
@Author: Nikita
@Date: 2022-04-19 16: 30: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 16:30:00
@Title:Write a Python program to get the difference between the two lists.
'''



if __name__=="__main__":
    first_list=[]
    n=int(input("Enter Number of element in first list: "))
    for i in range(0,n):
        first_list.append(int(input()))

    print(first_list)

    second_list=[]
    n=int(input("Enter Number of element in second list: "))
    for i in range(0,n):
        second_list.append(int(input()))
    print(second_list)

    second_list.extend(first_list)
    print("After appending first list in second list the list become: ",second_list)


    