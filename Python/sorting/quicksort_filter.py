#!/usr/bin/env python3
import random
import sys

"""
Quick sort as name suggest fastest start with O(nlog(n)) time it finishes sorting on average

How it works? Take a pivotal element normally first element, sort elements smaller than it to left
and bigger than it to other side  and repeat it. 

"""


def genarr(n):
    arr = []
    for i in range(n):
       num = random.randint(-9999991999, 9999999999)
       arr.append(num)
    return arr

def qsort(arr):
    if len(arr) == 0:
       return arr
    pivot = arr[0]
    small = [x for x in arr[1:] if x <= pivot]
    big  =  [x for x in arr[1:] if x > pivot]
    return qsort(small) + [pivot]  + qsort(big)

if __name__ == "__main__":
    print(sys.argv[0])
    print(sys.argv[1])
    if len(sys.argv) != 2:
       print("usage: sys.argv[0] num  num is the number of elements to sort out")
       # Exit the program
       sys.exit(100)
    if not isinstance(int(sys.argv[1]), int):
       print("Usage sys.argv[0] num num must be of integer type")
       sys.exit(101)
    arr = genarr(int(sys.argv[1]))
    print(arr)
    print(qsort(arr)) 
