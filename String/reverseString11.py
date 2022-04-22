'''
@Author: Nikita
@Date: 2022-04-18 12: 35: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-18 12:35:00
@Title: Write a Python program to reverse a string.
'''

# user_string=input("Enter a string: ")
# revStr=' '
# for i in user_string:
#     revStr=i+revStr

# print(revStr,end='')

if __name__=="__main__":
    user_input=input("Enter a string: ")
    result=user_input[: :-1]
    print("Reverse of string is: ",result)