'''
@Author: Nikita
@Date: 2022-04-18 11: 10: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-18 11:10:00
@Title:Write a Python function that takes a list of words and returns the length of the longest
one.
'''


def find_longest_string(string):
    """
        Description:
            Function to find longest word in string
        Parameter:
            Passing input string as a parameter
        Return:
            returning longest string
    """ 
    longestword=max(str1, key=len)
    return longestword

if __name__=="__main__":
    str=input("Enter a string: ")
    str1=list(str.split(" "))
    print(str1)

    print("Longest word in given string is: ",find_longest_string(str1))