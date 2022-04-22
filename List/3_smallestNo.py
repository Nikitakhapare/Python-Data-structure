'''
@Author: Nikita
@Date: 2022-04-19 15: 20: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 15:20:00
@Title:Write a Python program to get the smallest number from a list
'''
def smallest_no(lst):
    """
        Description:
            Function to calculate smallest Number among list of Elements
        Parameter:
            Pasing List as a parameter
        Return:
            returning smallest Number
    """ 

    small_no=lst[0]
    for i in range(1,len(lst)):
        if lst[i] < lst[0]:
            small_no=lst[i]
        
    print("Smallest No is: ",small_no)


if __name__=="__main__":
    my_list=[]
    n=int(input("Enter Number of element in list: "))
    for i in range(0,n):
        my_list.append(int(input()))

    print(my_list)
    smallest_no(my_list)
