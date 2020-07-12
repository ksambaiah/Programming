#!/usr/bin/env python

# Multiple of 3 below 1000


def mul3(n):
    mul3ben = [ x for x in range(n) if  x % 3 == 0 ]
    return mul3ben
def mul5(n):
    mul5ben = [ x for x in range(n) if  x % 5 == 0 ]
    return mul5ben

if __name__ == "__main__":
    arr = mul3(1000)
    arr1 = mul5(1000)
    unionset = set(arr)|set(arr1)
    print(sum(unionset))
