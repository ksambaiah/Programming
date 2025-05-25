#!/usr/bin/env python3
import sys
import argparse
import random
import numpy as np

"""
mergesort is nlog(n) algorithm.
"""

def get_args():
    parser = argparse.ArgumentParser(prog=sys.argv[0], description='Merging two sorted arrays')
    parser.add_argument('-n', dest='len', type=int, help='integer has to be provided', required=True)
    args = parser.parse_args()
    return args

def genarr(n):
    arr = []
    for i in range(n):
        num = random.randint(-9999991999999999999, 99999999999999999999999)
        arr.append(num)
    return arr

def mergeSort(arr):
    if len(arr) == 1:
       return arr
    r = len(arr) // 2
    print(r)
    mergeSort(arr[:r-1])
    mergeSort(arr[r:])
    merge(arr[:r-1], arr[r:])
def merge(arr1, arr2):
    mergearr = []
    i = j =  0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
           mergearr.append(arr1[i])
           i = i+1
        else:
           mergearr.append(arr2[j]) 
           j = j+1
    while i < len(arr1):
       mergearr.append(arr1[i])
       i = i+1
    while j < len(arr2):
       mergearr.append(arr2[j])
       j = j+1
    return mergearr
if __name__ == "__main__":
    args = get_args()
    l  = args.len
    arr =  genarr(l)
    print(arr)
    print(np.sort(arr))
    print(mergeSort(arr))
    
