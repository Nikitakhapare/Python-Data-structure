'''
@Author: Nikita
@Date: 2022-04-19 11: 25: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 11:25:00
@Title:Write a Python program for removing members to set
'''
from tokenize import maybe


my_set=set(['rk','l'])  
for i in range(2,9,2):
    my_set.add(i)
print("set is : ",my_set)
my_set.remove('rk')
my_set.pop()
print("After Removing Member set become: ",my_set)

