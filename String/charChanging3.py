'''
@Author: Nikita
@Date: 2022-04-18 09: 20: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-18 09:20:00
@Title: Write a Python program to get a string from a given string where all occurrences of its
        first char have been changed to '$', except the first char itself.
'''




def change_char(str):
    """
        Description:
            Function to change all occurance of first character
        Parameter:
            Passing input string as aParameter
        Return:
            returning sting by changing character
    """ 
    char = str[0]
    str = str.replace(char, '$')
    str = char + str[1:]   #slicing operation 

    return str
if __name__=="__main__":
    string=input("Enter a string: ")
    print("String Become: ",change_char(string))