'''
@Author: Nikita
@Date: 2022-04-21 11: 10: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 11:10:00
@Title:Write a Python program to print a dictionary in table format.

'''


dict1 = {(0, 0): 'niki', (0, 1): 21, (0, 2): 'Data structures',
         (1, 0): 'pari', (1, 1): 20, (1, 2): 'MySql',
         (2, 0): 'ved', (2, 1):21, (2, 2): 'OOPS with python'
}
 
print(" NAME " ," AGE " ,"  COURSE " )
 
# Iterate through the dictionary
for i in range(3):  
     
    for j in range(3):
        print(dict1[(i, j)], end ='   ')
         
    print()