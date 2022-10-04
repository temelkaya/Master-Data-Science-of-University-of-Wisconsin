"""
ds 710: Programming for Data Science
Assignment 1

Tem KYA

Do not rename this file
"""

### RUNNING CODE ###

# Put your cursor in the following line and press f9 to run it.
print("hello world")

#Note that you may also run a selected line of code by pressing the
#"Run selection or current line" button in the toolbar.

### QUICK PYTHON PREVIEW ###
## VARIABLES ##

#create a variable named a, and store the value 3+1 in it
a = 3+1

#display a
print(a)

#TASK 2.1
#Use f-string formatting
print(f'three plus one is 4 and that times four is 16')

#Changing first name & last name
first_name = "Tem" # you must change this line
last_name = "Kaya"
print(first_name+last_name)

#Alignment using tabs
print(f"Tem \tKaya \n{first_name} {last_name}")

#String Concatenation
print(first_name, last_name, sep=" ")

#Tab Completion
print(first_name.upper()+last_name.upper())

#TAB 2.2
def foo():
    return 42

foo()

t = foo()


import random
def make_message(first_name, last_name):
    if first_name in ["given",""] or last_name in ["surname",""]:
        raise ValueError("Unchanged or empty first or last name")
    greeting = f"Hi, {first_name} {last_name}, it is nice to meet you!"
    greeting = greeting + f" I'm Robot #{random.randint(0,1000000)}"
    
    print(greeting)
    return greeting


    if first_name in ["McKenzie",""] or last_name in ["West",""]:
        raise ValueError("Unchanged or empty first or last name")
    prof.greeting = f"Hi, {first_name} {last_name}, it is nice to meet you!"
    prof.greeting = prof.greeting + f" I'm Robot #{random.randint(0,1000000)}"
    
    print(prof.greeting)
    return prof.greeting