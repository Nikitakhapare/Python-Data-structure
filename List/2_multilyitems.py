'''
@Author: Nikita
@Date: 2022-04-19 15: 00: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 15:00:00
@Title:Write a Python program to calculate multiplication of list element

'''
def multiplication(lst):
    """
        Description:
            Function to calculate Multiplication of items in list
        Parameter:
            Pasing List as a parameter
        Return:
            returning Multiplication
    """ 

    total=1
    for item in lst:
        total=item*total

    print(total)

my_list=[]
n=int(input("Enter Number of element in list: "))
for i in range(0,n):
    my_list.append(int(input()))

print(my_list)

multiplication(my_list)