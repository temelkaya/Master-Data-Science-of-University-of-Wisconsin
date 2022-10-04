# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 19:29:13 2022

@author: temel
"""

# TASK2
# odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

for num in range(1, 30, 2):
    if(num>1):
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
            
# TASK 3

LoanAmt100000
LoanAPR=5
MonthlyPmt=500
PeriodicInrRare=LoanAPR/(100*12)
Balance=LoanAmt
month=0
totalInt=0
print("Month\tpayment\tIntreset\tBalance")
while(Balance>0):
    MonthlyPrincipal=int(MonthlyPmt-(Balance*PeriodicInrRare))
    MonthlyPrincipalDisplay=int(MonthlyPrincipal*100) / 100.0
    MonthlyIntPmt=int(MonthlyPmt-MonthlyPrincipal)
    MonthlyIntPmtDisplay=int(MonthlyIntPmt*100) / 100.0
    totalInt+=MonthlyIntPmt
    Balance=int(Balance-MonthlyPrincipal)
    BalanceDisplay=int(Balance*100) / 100.0
    if(Balance>0):
        month+=1
        print("{}\t{}\t\t{}\t\t{}".format(month,MonthlyPmt,MonthlyIntPmtDisplay,BalanceDisplay))
    else:
            month+=1
            print("{}\t{}\t\t{}\t\t0".format(month,MonthlyPmt,MonthlyIntPmtDisplay,BalanceDisplay))
            year=int(month/12)
            months=month%12
            totalPayment=LoanAmt+totalInt
            totalPaymentDisp=int(totalPayment*100) / 100.0
            print("Payback will takes {} years and {} months, and total amount paid approximately ${}".format(year,months,totalPaymentDisp))

# My comment: without using "round" comment I couldn't reach the correct number. This is my best approach solution


# TASK 3.2.1
LoanAmt=500
LoanAPR=5
MonthlyPmt=100
PeriodicInrRare=LoanAPR/(100*12)
Balance=LoanAmt
month=0
totalInt=0
print("Month\tpayment\tIntreset\tBalance")
while(Balance>0):
    MonthlyPrincipal=int(MonthlyPmt-(Balance*PeriodicInrRare))
    MonthlyPrincipalDisplay=int(MonthlyPrincipal*100) / 100.0
    MonthlyIntPmt=int(MonthlyPmt-MonthlyPrincipal)
    MonthlyIntPmtDisplay=int(MonthlyIntPmt*100) / 100.0
    totalInt+=MonthlyIntPmt
    Balance=int(Balance-MonthlyPrincipal)
    BalanceDisplay=int(Balance*100) / 100.0
    if(Balance>0):
        month+=1
        print("{}\t{}\t\t{}\t\t{}".format(month,MonthlyPmt,MonthlyIntPmtDisplay,BalanceDisplay))
    else:
            month+=1
            print("{}\t{}\t\t{}\t\t0".format(month,MonthlyPmt,MonthlyIntPmtDisplay,BalanceDisplay))
            year=int(month/12)
            months=month%12
            totalPayment=LoanAmt+totalInt
            totalPaymentDisp=int(totalPayment*100) / 100.0
            print("Payback will takes {} years and {} months, and total amount paid approximately ${}".format(year,months,totalPaymentDisp))

# My comment: without using "round" comment I couldn't reach the correct number. This is my best approach solution

#TASK 3.2.2
LoanAmt=500
LoanAPR=5
MonthlyPmt=500
PeriodicInrRare=LoanAPR/(100*12)
Balance=LoanAmt
month=0
totalInt=0
print("Month\tpayment\tIntreset\tBalance")
while(Balance>0):
    MonthlyPrincipal=int(MonthlyPmt-(Balance*PeriodicInrRare))
    MonthlyPrincipalDisplay=int(MonthlyPrincipal*100) / 100.0
    MonthlyIntPmt=int(MonthlyPmt-MonthlyPrincipal)
    MonthlyIntPmtDisplay=int(MonthlyIntPmt*100) / 100.0
    totalInt+=MonthlyIntPmt
    Balance=int(Balance-MonthlyPrincipal)
    BalanceDisplay=int(Balance*100) / 100.0
    if(Balance>0):
        month+=1
        print("{}\t{}\t\t{}\t\t{}".format(month,MonthlyPmt,MonthlyIntPmtDisplay,BalanceDisplay))
    else:
            month+=1
            print("{}\t{}\t\t{}\t\t0".format(month,MonthlyPmt,MonthlyIntPmtDisplay,BalanceDisplay))
            year=int(month/12)
            months=month%12
            totalPayment=LoanAmt+totalInt
            totalPaymentDisp=int(totalPayment*100) / 100.0
            print("Payback will takes {} years and {} months, and total amount paid approximately ${}".format(year,months,totalPaymentDisp))

# My comment: without using "round" comment I couldn't reach the correct number. This is my best approach solution

#TASK 3.2.3
LoanAmt=500
LoanAPR=5
MonthlyPmt=1
PeriodicInrRare=LoanAPR/(100*12)
Balance=LoanAmt
month=0
totalInt=0
print("Month\tpayment\tIntreset\tBalance")
while(Balance>0):
    MonthlyPrincipal=int(MonthlyPmt-(Balance*PeriodicInrRare))
    MonthlyPrincipalDisplay=int(MonthlyPrincipal*100) / 100.0
    MonthlyIntPmt=int(MonthlyPmt-MonthlyPrincipal)
    MonthlyIntPmtDisplay=int(MonthlyIntPmt*100) / 100.0
    totalInt+=MonthlyIntPmt
    Balance=int(Balance-MonthlyPrincipal)
    BalanceDisplay=int(Balance*100) / 100.0
    if(Balance>0):
        month+=1
        print("{}\t{}\t\t{}\t\t{}".format(month,MonthlyPmt,MonthlyIntPmtDisplay,BalanceDisplay))
    else:
            month+=1
            print("{}\t{}\t\t{}\t\t0".format(month,MonthlyPmt,MonthlyIntPmtDisplay,BalanceDisplay))
            year=int(month/12)
            months=month%12
            totalPayment=LoanAmt+totalInt
            totalPaymentDisp=int(totalPayment*100) / 100.0
            print("Payback will takes {} years and {} months, and total amount paid approximately ${}".format(year,months,totalPaymentDisp))

# My comment: It became infinity 

#TASK 3.3

LoanAmt=250000
LoanAPR=4
MonthlyPmt=1000
PeriodicInrRare=LoanAPR/(100*12)
Balance=LoanAmt
month=0
totalInt=0
print("Month\tpayment\tIntreset\tBalance")
while(Balance>0):
    MonthlyPrincipal=int(MonthlyPmt-(Balance*PeriodicInrRare))
    MonthlyPrincipalDisplay=int(MonthlyPrincipal*100) / 100.0
    MonthlyIntPmt=int(MonthlyPmt-MonthlyPrincipal)
    MonthlyIntPmtDisplay=int(MonthlyIntPmt*100) / 100.0
    totalInt+=MonthlyIntPmt
    Balance=int(Balance-MonthlyPrincipal)
    BalanceDisplay=int(Balance*100) / 100.0
    if(Balance>0):
        month+=1
        print("{}\t{}\t\t{}\t\t{}".format(month,MonthlyPmt,MonthlyIntPmtDisplay,BalanceDisplay))
    else:
            month+=1
            print("{}\t{}\t\t{}\t\t0".format(month,MonthlyPmt,MonthlyIntPmtDisplay,BalanceDisplay))
            year=int(month/12)
            months=month%12
            totalPayment=LoanAmt+totalInt
            totalPaymentDisp=int(totalPayment*100) / 100.0
            print("Payback will takes {} years and {} months, and total amount paid approximately ${}".format(year,months,totalPaymentDisp))
