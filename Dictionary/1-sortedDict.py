'''
@Author: Nikita
@Date: 2022-04-21 04: 20: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 04:20:00
@Title:Write a Python script to sort (ascending and descending) a dictionary by
value.
'''

import operator
my_dict = {1: 23,2: 67,4: 12,3: 90}
print(my_dict)
 
# Sorting dictionary
sorted_dict = sorted(my_dict.items(), key = operator.itemgetter(1))
 
# Printing sorted dictionary
print("Sorted dictionary in assending order is :",sorted_dict)

sorted_dict = sorted(my_dict.items(), key = operator.itemgetter(1), reverse=True)
print("Sorted dictionary in desending order is :",sorted_dict)
