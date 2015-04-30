# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:41:19 2015

@author: tridibdutta
"""

import itertools
def erat2( ):
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p



##=========================================================##

import itertools
def primes_less_than(N):
    primes = [x for x in (2,3,5,7,11,13) if x < N]
    #print primes
    if N < 17: 
        return primes
    
    candidates = [x for x in xrange((N-2)|1,15,-2) 
                    if x%3 and x%5 and x%7 and x%11 and x%13]
    
    #print candidates

    top = int(N ** 0.5)
    while (top+1)*(top+1) <=N:
        top +=1
    
    while True:
        p = candidates.pop()
        primes.append(p)
        if p > top:
            break
        candidates = filter(p.__rmod__, candidates)

    candidates.reverse()
    primes.extend(candidates)
    return primes
                    
                        
                    
                        
    
    