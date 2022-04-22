'''
@Author: Nikita
@Date: 2022-04-19 18: 50: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 18:50:00
@Title:Write a Python program to find common elements among two lits
'''


def common_elements():
    """
        Description:
            Function to find common items in two lists list
        Parameter:
            no parameter
        Return:
            returning common elements
    """ 
    common=[]
    for i in first_list:
        if i in second_list:
            common.append(i)
    
    print("Common Element Among 2 lists are : ",common)
        

if __name__=="__main__":
    first_list=[]
    n=int(input("Enter Number of element in first list: "))
    for i in range(0,n):
        first_list.append(int(input()))

    print(first_list)

    second_list=[]
    n=int(input("Enter Number of element in second list: "))
    for i in range(0,n):
        second_list.append(int(input()))
    print(second_list)

    common_elements()


    
    