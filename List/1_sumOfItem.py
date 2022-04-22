'''
@Author: Nikita
@Date: 2022-04-19 14: 50: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 14:50:00
@Title:Write a Python program to get the sum of number from a list
'''

try:
    my_list=[]
    print("Enter a Elemnt of list: ")
    while True:
        my_list.append(int(input()))

except:
    print(my_list)

sum=0
for i in my_list:
    sum=i+sum

print("Sum of Elements is: ",sum)