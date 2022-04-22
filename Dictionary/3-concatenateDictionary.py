from cgitb import reset


'''
@Author: Nikita
@Date: 2022-04-21 04: 50: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 04:50:00
@Title:Write a Python script to concatenate following dictionaries to create a new
one.

'''


def concatinate(dic1,dic2):
    return(dic1.update(dic2))


if __name__=="__main__":
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}

    concatinate(dic1,dic2)
    concatinate(dic1,dic3)

    print("Aftyer Concanating Dictionaries dic1 become: ",dic1)