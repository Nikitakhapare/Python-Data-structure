'''
@Author: Nikita
@Date: 2022-04-18 12: 10: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-18 12:10:00
@Title: Write a python program to find number of occurrences of substring in given string
'''


#finding number of occurrences of substring in given string
def occurance_of_string():
    """
        Description:
            Function to count the occurance of sub String in string
        Parameter:
            No Parameter
        Return:
            returning Number of ocuurance of string
    """ 
    input=inputStr.lower()
    subString=inputSubStr.lower()
    count = input.count(subString)

    print("Number of occurrences of substring :", count)

if __name__=="__main__":
    inputStr=input("Enter a string: ")
    inputSubStr=input("Enter a sub String: ")
    occurance_of_string()