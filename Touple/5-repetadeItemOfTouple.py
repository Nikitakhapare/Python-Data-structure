'''
@Author: Nikita
@Date: 2022-04-19 10: 55: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 10:55:00
@Title:Write a Python program to find the repeated items of a tuple
'''
if __name__=="__main__":

    myTouple=(1,3,4,32,1,1,1,31,32,12,21,2,3) 
    newList=[] 
    for i in myTouple:
        if myTouple.count(i) > 1:
            if i in newList:
                continue
            else:
                newList.append(i)

    print(newList)