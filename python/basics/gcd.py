#!/usr/bin/env python

import random

# Computing GCD of two numbers, how do we get two positive integers?
# Using Random integers
def gcd(i, j):
    if j == 0:
       return i
    else:
       return gcd(j, i%j) 

if __name__ == "__main__": 
   a = random.randint(1, 999999999999)
   b = random.randint(1, 999999999999)
   if a > b:
      r = gcd(a, b)
   else:
      r = gcd(b, a)
   print("GCD of % d and % d is % d" %(a, b, r))
