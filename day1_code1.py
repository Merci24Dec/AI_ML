# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 11:23:19 2020

@author: anshu
"""
x= 5
y = 6
print(x+y)

# i am comment
'''
i am in a multiline comment
i am also in a same multiline comment area
'''

'''
1. Data Types
    - primitive - int, str, float, bool, complex
    - non-primitive - list, tuple, set, dictionary
    
2. Control Flow
    - if else
    - for loop
    - while loop
3. Functions
     - built in functions
     - user defined functions
4. Object Oriented programming
'''
#################################################
# 1. Data Types
#   - primitive data types
x = 5
type(x)

y = 25.0
type(y)

z = "Hello from World from ME"
type(z)

z.upper()
z.lower()
z.split()

k = True
type(k)
not k


m = 5 + 6j
type(m)
m.conjugate()
m.imag
m.real

#####################################
#2. Non primitive - list, tuple, set, dict

###########################################
# LIST
'''
 - collection of values
 - can be defined using [] (square) brackets
 - supports elements of multiple data types
 - supports repeation of values
'''
x = [4,5,2.3,45,'hii','bye',12,4]
# to check the length of list
len(x)
# indexing
x[0]
x[1]
x[4]
x[-2]
x[-3] == x[5]
# Slicing
x[1:4]
x[0:3]
x[-7:-2]
########### Customizing
print(x)
x[1] = 11
print(x)
x[1],x[2] = 25,50
x[1:3]=14,13
x.append(6)# to add a new value at the end of list
x.extend([7,'hello',12,3])
print(x)
x.insert(3,'hibye')# to add value at a location

x.remove('hii')# to remove any value
x.remove(x[3])
x.pop(3)

##############################################
# Tuple
'''
 - collection of values
 - supports repeation, values of different types
 - can be defined using () parenthesis, small bracket
'''
y = (4,5,2.5,'hii','hello','bolo',12)
type(y)
len(y)
# indexing
y[0]
y[2]
y[-1]
y[-3]
# slicing
y[1:3]
y[2:6]
y[-5:-2]
# customizing
print(y)
y[1] = 25

##############################################
# Dictionary
# collection of key vlaue pair in {} brackets
z = {"name":"Anshu","age":22,"laptop":"hp"}
type(z)
#indexing
z['name']
z['age']
#customizing
z['country'] = "India"
print(z)
z.pop('age')
print(z)
#################################
#set 
# defined using {}, no repeation
# used for set theory related operation
a = {1,5,4,2,5,4,2,5,4,2,5,8}
print(a)
type(a)

b = {8,9,5,4,7,5,5,6,6,3,2}
print(b)

a.union(b)
a.intersection(b)

############################################
#############################################
# write a program to add two numbers
# show the result

a = input("Enter the first number ")
b = input("Enter the second number ")
c = int(a)+int(b)
print('The addition is ',c)

#**************************
# BMI calculator
w = input('Enter the weight in KG ')
h = input("Enter the height in CM ")
h = int(h)/100
bmi = int(w)/(h*h)
print(bmi)

if bmi<25:
    print("Your bmi is low")
    print("you should join some food festival")
elif bmi>=25 and bmi<30:
    print("you are fit")
    print("Stay fit and stay happy")
    print("start a youtube channel on fitness")
else:
    print("you are overweight")
    print("use stairs more and lift less")
    print("Join Civil Engineering or mechanical")
    
# ****************************************** #

# for loop

for i in range(5):
    print("Hello from python")

for i in range(5):
    print("hello world ",i)

for i in range(3,12):
    print("hello world ",i)

for i in range(3,12,2):
    print("hello world ",i)

for i in range(12,3,-1):
    print("hello world ",i)


temp = [25,26,24,25,26,27,28,26,26,25,28,29,24,25]
for val in temp:
    if val>26:
        print(val)


# list comprehension
k = [i for i in temp if i>26]
print(k)

##########################################
# while loop
x = 3
while x<20:
    print('python is awesome')
    x = x+1

x = 2
while True:
    print('python is amazing')
    x = x + 1
    if x>25:
        break

###################################################
###################################################
# Functions in python
# builtiin functions
    
a = [4,5,6,8]
sum(a)
min(a)
max(a)
b = 45.12656247
round(b,3)
k = [78,23,56,12,45,89,56,23,45]
sorted(k)

m = ['hi','hello','bye','why','shy','fly','what']
sorted(m,key=len)

help(sorted)

###################################################

def fun1():
    print("i am a function")
    print('my name is fun1')
    
fun1()


def fun2(a,b):
    "i am function "
    c = a + b
    print(c)
    
fun2(7,8)

def fun3(a,b=3):
    """ This function can be used to add two numbers
    >> fun3(7,3)
    >> 10
    """
    c = a + b
    return c

fun3(7,3)
print(fun3.__doc__)
help(fun3)
fun3(5,4)
fun3(9)

#################################################

class A:
    x = 5
    y = 6
    
    def fun4(self):
        print("i am a function of class A")
    
    def fun5(self,a,b):
        print("i am a function of class A, fun5")
        return a+b
    
k = A()
k.x
k.y
k.fun4()
k.fun5(4,6)

m = A()
m.x
m.y





        
        






























