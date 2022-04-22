'''
@Author: Nikita
@Date: 2022-04-21 10: 30: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-19 10:30:00
@TitleWrite a Python program to print all unique values in a dictionary.
Sample Data 
'''



dict_list =  [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

my_dict = []
for i in dict_list:
    for val in i.values():
        my_dict.append(val)

print("Orignal Dictionary Is: ", dict_list)
print("")
print("Printing Unique Values From Dictionary Is: ", my_dict)