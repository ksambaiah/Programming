#!/usr/bin/env python3

# GCD of two numbers

def gcd(m, n):
    if n == 0:
       return m
    return gcd(n, m%n)

if __name__ == "__main__":
    a = 324529
    b = 71
    print("gcd of {0} and {1} is computed".format(a, b))
    print(gcd(a, b))
