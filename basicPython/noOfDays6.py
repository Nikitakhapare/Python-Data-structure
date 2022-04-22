'''
@Author: Nikita
@Date: 2022-04-18 2: 27: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-18 2:27:00
@Title: Calculate days Between to Dates
'''

from datetime import date


def no_of_days(date1,date2):
    """
        Description:
            Function to Calculate Days between two Dates
        Parameter:
            Passing Date1 and  Date 2 as a Parameter
        Return:
            returning No of days
    """
    no_of_days=(date2-date1)
    return(no_of_days).days
    

date1=date(2014, 7, 2)
date2=date(2014, 7, 11)
print("Days between to dates are ",no_of_days(date1,date2))