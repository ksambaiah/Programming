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

def qsort(arr):
    if len(arr) == 0:
       return arr
    pivot = arr[0]
    small = [x for x in arr[1:] if x <= pivot]
    big  =  [x for x in arr[1:] if x > pivot]
    return qsort(small) + [pivot]  + qsort(big)

def get_args():
    parser = argparse.ArgumentParser(prog='quicksort_filter.py', description='quicksort program sorts array of given length')
    parser.add_argument('-n', dest='len', type=int, help='integer has to be provided', required=True)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_args()
    arr = genarr(args.len)
    print("array after generating elements before sorting.")
    print(arr)
    print("array after doing quicksort")
    print(qsort(arr)) 
