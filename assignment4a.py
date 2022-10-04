# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 21:32:49 2022

@author: temel
"""

#Task 2. Average Maximus From a List of Tuples
#Subtask 2.1: Finding Maximums
#Subtask 2.2 Test your Function

def get_maximums(tuple_list):
#Find out maximum from each tuple lists
    return [max(x) for x in tuple_list]

def average_of_maximums(tuple_list):
#Finding maximums from each tuple and get the average
    return sum(get_maximums(tuple_list))/len(tuple_list)

if __name__ == '__main__':

    test_list1 = [(1,2,3),(4,5,6)]
    test_list2 = [(4.1, -3, 6), (-6, 2.0001, 10), (9/5, -5, 8/9), (-2, -7, 2, 7, 8, 2)]
    test_list3 = [(1.1,1.2,-1.3)]
    test_list4 = [(0,)]

    print('get_maximums('+str(test_list1)+') = '+str(get_maximums(test_list1)))
    print('get_maximums('+str(test_list2)+') = '+str(get_maximums(test_list2)))
    print('get_maximums('+str(test_list3)+') = '+str(get_maximums(test_list3)))
    print('get_maximums('+str(test_list4)+') = '+str(get_maximums(test_list4)))
#Subtask 2.3 Averaging the Maximumus
    print('average_of_maximums('+str(test_list1)+') = '+str(average_of_maximums(test_list1)))
    print('average_of_maximums('+str(test_list2)+') = '+str(average_of_maximums(test_list2)))
    print('average_of_maximums('+str(test_list3)+') = '+str(average_of_maximums(test_list3)))
    print('average_of_maximums('+str(test_list4)+') = '+str(average_of_maximums(test_list4)))
    
#Task 3: Time Until Midnight

from datetime import datetime

def minutes_to_midnight():
#using datetime.now() to reach hours minutes and seconds of current time
    hours = int(datetime.now().strftime("%H"))
    min = int(datetime.now().strftime("%M"))
    sec = int(datetime.now().strftime("%S"))
#if second is not 0 (zero) then minis 1 min
    if sec != 0:
        total_min = ((24-hours)*60)-min-1
#else do not cchange
    else:
        total_min = ((24-hours)*60)-min
    return total_min

#calling the code of  "minutes_to_midnight function"
min = minutes_to_midnight()


#Task 4:Mortgage Calculator Revisited
def amortization (principal, monthly_payment, rate):
    
    balance = principal
    di = {}
    table = []
    mnth = 0 
    total = 0 
    if monthly_payment > principal * rate / 12:
        while (balance > 0):
            mnth += 1 
            interest = balance * rate / 12 
            balance = balance + interest - monthly_payment
            if balance < 0:
                monthly_payment += balance 
                balance = 0
            total += monthly_payment
            table.append ([mnth, monthly_payment, interest, balance])
    di ["total_paid"] = total
    di ["number_of_months"] = mnth
    di ["am_table"] = table
    return di
di["total_paid"]=




