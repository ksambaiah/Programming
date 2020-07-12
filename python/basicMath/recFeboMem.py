#!/usr/bin/env python

# Compute fibonacci number

def fib(f, d, n):
    if n == 1:
       return f
    else:
       return fib(f+d, f, n-1)
      

if __name__ == "__main__":
   d = 42
   fibn = fib(1,0,d)
   print("Fibonacci number of %d is %d" %(d, fibn))
