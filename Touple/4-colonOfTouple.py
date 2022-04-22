'''
@Author: Nikita
@Date: 2022-04-19 10: 55: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 10:55:00
@Title:Write a Python program to create the colon of a tuple
'''
if __name__=="__main__":

    #create a tuple
    myTouple = ("Red","Green", 5, []) 
    print(myTouple)
    #Creating Copy of Touple
    myToupleCopy = myTouple
    myToupleCopy[3].append(6)
    myToupleCopy[3].append(5)    
    print(myToupleCopy)
    print(myTouple)
