'''
@Author: Nikita
@Date: 2022-04-19 11: 25: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 11:25:00
@Title:Write a Python program for adding elements to set
'''
s=set(['rk','l'])   
s.add(1)
s.add("pari")
s.add(6)
s.add("niki")
s.add("s")

#Adding element to the set using loop
for i in range(3,8,2):
    s.add(i)
print("After adding the Elements Set Become: ",s)