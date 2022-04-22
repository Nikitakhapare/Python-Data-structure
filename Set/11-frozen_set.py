'''
@Author: Nikita
@Date: 2022-04-19 08: 50: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 08:50:00
@Title:Write a Python program for use of frozen set
'''
s={'red','black','green'}  
set=frozenset(s)
print("Frozen set is : ",set)
set.add('blue')
print(set)