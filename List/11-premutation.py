'''
@Author: Nikita
@Date: 2022-04-19 16: 55: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 16:55:00
@Title:Write a Python program to generate all permutations of a list in Python

'''
list1=[1,2,5,4]
list2=[2,6,3,1]

print("Original List are: ",str(list1)+str(list2))
print("All Premutations are: ")
for i in list1:
    for j in list2:
        res_list=[i,j]

        print(res_list,end=" ")
