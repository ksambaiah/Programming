#!/usr/bin/env python3

# Factorial of numbers
# This is simple program.

def fact(n):
    if n == 1:
       return n
    return n * fact(n-1)

if __name__  == "__main__":
     n = 10
     print("Factorial of {0}".format(n))
     print(fact(n))
