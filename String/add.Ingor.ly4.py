'''
@Author: Nikita
@Date: 2022-04-18 09: 20: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-18 09:20:00
@Title:Write a Python program to add 'ing' at the end of a given string (length should be at
        least 3). If the given string already ends with 'ing' then add 'ly' instead. I
'''
str=input("Enter a string: ")
if len(str) < 3:
    print("Enter a String with less than three character. ")

else:
    if str[-1]=='g' or str[-2]=='n' or str[-3]=='i':
        str=str+"ly"
    
    else:
        str=str+'ing'

print("After Making changes the given string become: ",str)
