# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 14:37:58 2022

@author: temel
"""
#Task 2: Filename Verification
#Subtask 2.1: Function with two inputs

def filename_checker(ext,name):
    nameExt = name.split(".")[1]
    if nameExt==ext:
        return name
    else:
        return name+"."+ext

print(filename_checker('csv','my_csv.csv'))
print(filename_checker('txt','my_csv.csv'))

#Subtask 2.2: Currying for specific filetypes
def as_csv(txt):
    return txt+".csv"

def as_txt(txt):
    return txt+".txt"

print(as_csv('foo'))
print(as_txt('foo.bar'))

#Task 3: Mortgage Calculator Continued
#Subtask 3.1: Multiple Outputs and Errors
def amortization(principal, monthly_payment, interest_rate):
   total_paid=0
   I=interest_rate
   MP=monthly_payment
   while I >= 1:
       I = I/(100)  
   month = 0
   while principal > 0:
       print( month, "\t",MP,"\t",I,"\t", principal)
       principal = principal * ( 1 + I/12)
       month = month + 1
       if principal < MP:
               MP=principal    
       principal = principal - MP
       total_paid = total_paid + MP
       length_of_loan=month
   my_table={}    
   my_table["total_paid"]=total_paid
   my_table["number_of_months"]=length_of_loan
   my_table["am-table"]=[month,MP,I,principal]
   return my_table

amortization(500,100,5)

#Subtask 3.2: Saving to a csv

def as_csv(name):
    return filename_checker('csv',name)
def as_txt(name):
    return filename_checker('txt',name)

#Task 4: Matrix Multiplication

def dot_product(row,column):
	result = sum(map(lambda x,y: x *y ,row, column)) 
	return result

def matrix_multiplication(A,B):
	C = []
	TB = []
	for j in range(len(B[0])):
		temp=[]
		for i in range(len(B)):
			temp.append(B[i][j])
		TB.append(temp)
	if(len(A)!=len(TB)):
		raise Exception("Matrix Multiplication is not possible because row of A is not equal to column of B")
	else: 
		for i in range(len(A)):
			temp = []
			for j in range(len(TB)):
				temp.append(dot_product(A[i],TB[j]))
			C.append(temp)
	return C
