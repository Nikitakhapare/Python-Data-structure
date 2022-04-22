'''
@Author: Nikita
@Date: 2022-04-19 15: 20: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 15:20:00
@Title:Write a Python program to find longer word than n in list of word
'''

my_list=["apple","banana","Orange","Graphas"]
n=int(input("Enter a Value of n: "))
new_list=[]
for i in my_list:
    if len(i) > n:
        new_list.append(i)

print(new_list)