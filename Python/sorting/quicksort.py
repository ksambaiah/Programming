#!/usr/bin/env python3
import random
import sys
import argparse

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

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
           i = i+1
           (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i+1], arr[end]) = (arr[end], arr[i+1])
    return i+1
    
def qsort(arr, start, end):
    if start < end:
       r = partition(arr, start, end)
       qsort(arr, start, r-1)
       qsort(arr, r+1, end)
    return arr

def get_args():
    parser = argparse.ArgumentParser(prog='quicksort.py', description='quicksort program sorts array of given length')
    parser.add_argument('-n', dest='len', type=int, help='integer has to be provided', required=True)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_args()
    arr = genarr(args.len)
    print("Array before sorting of length ", len(arr))
    print(arr)
    print("Array after sorting")
    print(qsort(arr, 0, len(arr)-1)) 
    sys.exit(0)
