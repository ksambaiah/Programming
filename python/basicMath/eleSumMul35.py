#!/usr/bin/env python

# Multiple of 3 or 5 below 1000 and sum


def summul35(a,b,n):
    return sum([ x for x in range(n) if  x % 3 == 0 or x % 5 == 0])

if __name__ == "__main__":
    sum = summul35(3,5,1000)
    print(sum)
