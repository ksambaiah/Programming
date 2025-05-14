#!/usr/bin/env python3
import sys

# Fib number Fib0 = fib1 = 1 otherwise fibn = fib(n-1) + fib(n-2)
#Recursive is very very bad for this one.
# This is dynamic programming

def fib(n):
    arr = [1, 1]
    if n < len(arr):
       return arr[n]
    for j in range(len(arr), n+1):
        arr.append(arr[j-1] + arr[j-2])
    return arr[n]

if __name__ == "__main__":
    if (len(sys.argv) != 2 ):
       print("sys.argv[0] integer to run the program")
       sys.exit(1)
    print("This is called dynamic programming, faster than recursion")
    print(fib(int(sys.argv[1])))
