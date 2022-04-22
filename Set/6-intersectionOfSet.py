'''
@Author: Nikita
@Date: 2022-04-20 07: 30: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-20 07:30:00
@Title:Write a Python program for creating intersection of set
'''

if __name__=="__main__":
    set1={1,5,2,6,8}
    set2={6,9,5,7,3}
    set3={6,8,4,3}
    b=set2.intersection(set3)
    a=set1.intersection(set2)
    print("Intersection of sets are: ",a)
    print("Intersection of sets are: ",b)