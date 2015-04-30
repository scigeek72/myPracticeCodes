# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:14:16 2015

@author: tridibdutta

NOTE: THESE AREN'T EFFICIENT IMPLEMENTATION
FOR AN EFFICIENT AND FAST IMPLEMENTATION, LOOK AT THE FILE
primes_less_than.py
"""
#n>0
import math
def is_prime(n):
    if n <2:
        return False
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            return False
    
    return True
    

def getAllPrimes(n):
    c =[]
    for i in range(1,n,2):
        if is_prime(i):
            c.append(i)
    
    return c       
            

def countPrimes( n):
        numbers = set(range(n,1,-1))
        primes = []
        while numbers:
            p = numbers.pop()
            primes.append(p)
            numbers.difference_update(set(range(2*p,n+1,p)))
        return primes
               