#!/usr/bin/env python3
import random
import sys

# Generates two random numbers and computes gcd.

def gen():
   #return random.randint(1,999999999999)
   return random.randint(1,200)

def gcd(m, n):
    if n == 0:
      return m
    print(n, m%n)
    return gcd(n, m%n)

if __name__ == "__main__":
    (m, n) = (gen(), gen())
    print("Two numbers are {} and {}".format(m, n))
    if m <= n:
       print(gcd(n, m))
    else:
       print(gcd(m, n))
    
    
