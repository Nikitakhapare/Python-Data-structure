from itertools import count


'''
@Author: Nikita
@Date: 2022-04-19 18:20: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 18:20:00
@Title:Write a Python program to count the number of strings where the string length
        is 2 or more and the first and last character are same from a given list of strings.
'''


my_list=['abc', 'xyz', 'aba', '1221']
count=0
for i in my_list:
    if len(i) > 2 and i[0]==i[-1]:
        count+=1
    
print("count of string where the first and last character are same: ",count)