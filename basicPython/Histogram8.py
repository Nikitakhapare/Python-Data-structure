'''
@Author: Nikita
@Date: 2022-04-18 2: 27: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-18 2:27:00
@Title: creating Histogram from given list of integer
'''


def histogram( intNumbers ):
    for i in intNumbers:
        output=''
        num=i
        while(num > 0):
            output+='*'
            num=num-1
        print(output)

histogram([2,4,6,3])



