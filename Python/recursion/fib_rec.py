#!/usr/bin/env python3
import sys

# Fib number Fib0 = fib1 = 1 otherwise fibn = fib(n-1) + fib(n-2)
#Recursive is very very bad for this one.

def fib(n):
    if n == 0 or n == 1:
       return 1
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    if (len(sys.argv) != 2 ):
       print("sys.argv[0] integer to run the program")
       sys.exit(1)
    print("Running slow fib number for ", sys.argv[1])
    print(fib(int(sys.argv[1])))
