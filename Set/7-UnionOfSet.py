'''
@Author: Nikita
@Date: 2022-04-20 07: 40: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-20 07:40:00
@Title:Write a Python program for creating union of set
'''

if __name__=="__main__":
    set1={1,5,2,6,8}
    set2={6,9,5,7,3}
    set3={9,3,7,6}
    a=set2.union(set3)
    b=set1.union(set2)
    print("Union of sets are: ",a)
    print("union of set are: ",b)