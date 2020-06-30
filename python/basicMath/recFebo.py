#!/usr/bin/env python

# Compute fibonacci number

def fib(n):
    if (n < 2):
       return n
    else:
       return (fib(n-1) + fib(n-2))

if __name__ == "__main__":
   d = 20
   fibn = fib(d)
   print("Fibonacci number of %d is %d" %(d, fibn))
