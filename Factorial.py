# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 05:34:43 2019

@author: Anupama Dhir
"""

def factorial(n):
    fact=1
    num = n
    if (n == 0):
        fact = 1
   
    while (n > 1):
        fact = fact * n
        n -= 1
    print ("This method uses loops")    
    print ("Factorial of {} is {}:".format(num, fact))

num = int(input("Enter the number for finding factorial: "))
factorial (num)


def fact_recursion(n):
    if n <= 0:
        return 1
    else:
        return n * fact_recursion(n-1)

num = int(input("Enter the number for finding factorial: "))
f = fact_recursion(num)
print ("This method uses recursion") 
print ("factorial of {} is {}".format(num, f))

