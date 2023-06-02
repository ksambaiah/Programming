#!/usr/bin/env python3

# fib num in recursion is not good.

def fib(n):
    if n == 1 or n == 0:
       return n
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    n = 35
    print("Fib of number {0} is".format(n))
    print(fib(n))
