'''
@Author: Nikita
@Date: 2022-04-21 11: 30: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 11:30:00
@Title:Write a Python program to convert a list into a nested dictionary of keys.
'''


def dicMaker(list):
    res_dict={my_list[i]:my_list[i+1] for i in range(0,len(my_list),2)}
    return res_dict

my_list=['a',12,'b',2,'c',6,'d',9]
print("Dictionary Become: ",dicMaker(my_list))