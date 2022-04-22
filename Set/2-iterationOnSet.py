'''
@Author: Nikita
@Date: 2022-04-19 11: 15: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 11:15:00
@Title:Write a Python program for iterating set 
'''


my_set={"red","pink","yellow","blue"}
#using for
print("Elements of set are: ")
for item in my_set:
    print(item,end=" ")

#using enumerate

for counter,item in enumerate(my_set):
    print(counter, ":",item)