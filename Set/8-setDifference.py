'''
@Author: Nikita
@Date: 2022-04-20 07: 30: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-20 07:30:00
@Title:Write a Python program for creating set difference
'''

if __name__=="__main__":
    set1={1,5,2,6,8}
    set2={6,9,5,7,3}
    a=set1.difference(set2)
    print("Difference of sets are: ",a)