'''
@Author: Nikita
@Date: 2022-04-19 16: 30: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 16:30:00
@Title:Write a Python program to get the difference between the two lists.
'''
list1=[2,3,4,5,8,9]
list2=[2,3,4]
list=[]
for i in list1:
    if i not in list2:
        list.append(i)

print("Difference Between Two lists are: ",list)