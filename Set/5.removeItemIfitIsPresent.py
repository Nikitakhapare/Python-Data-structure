'''
@Author: Nikita
@Date: 2022-04-19 11: 25: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 11:25:00
@Title:Write a Python program for removing item if it is present
'''


my_set=set(['rk','l',"5","6","8","niki","ved","pari"])
user_input=input("Enter a itme you want to remove: ")
res=(my_set.__contains__(user_input))
if res == True:
    my_set.remove(user_input)
    print("After Removing set become: ",my_set)

else:
     print("item not in list: ")
