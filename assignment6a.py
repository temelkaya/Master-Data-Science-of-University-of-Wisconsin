# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:20:53 2022

@author: temel
"""
#Task 2: Correlation Coefficient
import math

# calculating correlation coefficient.
def corr_coeff(x, y):
    #calculating length
    length = len(x)

    # calculation types of summation for the formula
    sumx = sum(x)
    sumy = sum(y)
    sumxy = sum([x[i] * y[i] for i in range(length)])
    squareSumx = sum([x[i] * x[i] for i in range(length)])
    squareSumy = sum([y[i] * y[i] for i in range(length)])

    #calculating correlation coefficient.
    corr = (float)(length * sumxy - sumx * sumy) / (float)(math.sqrt((length * squareSumx -
                                                                    sumx * sumx) * (length * squareSumy -
                                                                                      sumy * sumy)))
    return corr


#testing the function
x = [41, 19, 23, 40, 55, 57, 33]
y = [94, 60, 74, 71, 82, 76, 61]


#calling
print("Correlation Coefficient for array x ", x, " and y ", y, " is")
print(corr_coeff(x, y))

#Task 3: Matrix Column Statistics

import numpy as np

#numpy arrays
test1 = np.array([[12,34,53],[34,35,np.NaN],[56,3,4]])
test2 = np.array([[1],[2],[45],[4]])
test3 = np.array([[1,np.nan,3]])

#outputs:
output1 = np.array([[34, 12, 56, 0],[24, 3, 35, 0], [19, 4, 53, 1]])
output2 = np.array([[13, 1, 45, 0]])
output3 = np.array([[1, 1, 1, 0],[np.nan, np.nan, np.nan, np.nan], [3, 3, 3, 0]])

#column_statistics function 
def column_statistics(arr):
    shape = arr.shape
    altered_array = []
    for i in range(0,shape[1]):
        #for col_i
        temp_mean = 0
        NaN_counter = 0
        temp_col = arr[:,[i]]
        for j in temp_col:
            if not np.isnan(j):
                temp_mean += j[0]
            
            if np.isnan(j):
                NaN_counter +=1 
        mean = temp_mean/temp_col.shape[0]
        if NaN_counter == temp_col.shape[0]:
            altered_array.append([np.nan,np.nan,np.nan,np.nan])
            continue
        altered_array.append([mean,min(temp_col)[0],max(temp_col)[0],NaN_counter])
    return np.array(altered_array)
             
#verifying the output with the function output

print("\n",column_statistics(test1) == output1)

print("\n",column_statistics(test2) == output2)

print("\n",column_statistics(test3) == output3)

#this will pop false because np.nan == np.nan will result to false output
np.nan == np.nan

#saving numpy arrays
with open('test_data.npy','wb') as npf:
    np.save(npf, test1)
    np.save(npf, test2)
    np.save(npf, test3)

#loading the save data
with open('test_data.npy','rb') as npf:
    l1 = np.load(npf)
    l2 = np.load(npf)
    l3 = np.load(npf)

#declaring
results1 = column_statistics(l1)
results2 = column_statistics(l2)
results3 = column_statistics(l3)

#saving the final result
with open('test_results.npy','wb') as npr:
    np.save(npr,results1)
    np.save(npr,results2)
    np.save(npr,results3) 
    
#Task 4: Polynomial evaluation
import numpy as np
def evaluate_polynomial(coeffs, x):
  # Get shape
  m,n= coeffs.shape
  # array of powers based on degree of evaluate_polynomial i.e degree n=4, [0,1,2,3]
  powers = np.array(range(n))
  # raise each value of x to powers based on coeffs
  # array of [x**0,x**1,x**2,...x**n]
  raised_x = np.apply_along_axis(lambda x:x**np.flip(powers),1,x)
  # multiply coeff to raised powers of x
  poly_val = np.sum(coeffs*raised_x,axis=1).reshape(-1,1)
  # return the polynomial value
  return poly_val

A = np.array([[10, 20, 30, 40],[0, 2, 4, 6]])
x = np.array([[-1],[2]])
print(evaluate_polynomial(A,x))

A = np.array([[3,2,1]])
x = np.array([[2]])
print(evaluate_polynomial(A,x))