'''
@Author: Nikita
@Date: 2022-04-19 15: 40: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 15:40:00
@Title:Write a Python program to remove Duplicates from list

'''

if __name__=="__main__":
    my_list=[2,3,4,2,6,2,5,8,6]
    newList = []
    for i in my_list:
        if i not in newList:
            newList.append(i)

    print("After Removing Duplicates List Become: ",newList)