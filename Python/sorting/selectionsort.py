#!/usr/bin/env python3
import random
import sys
import argparse

"""
selection sort n^{2} algorithm


"""


def genarr(n):
    arr = []
    for i in range(n):
       num = random.randint(-9999991999, 9999999999)
       arr.append(num)
    return arr

def ssort(arr):
    
    return arr

def get_args():
    parser = argparse.ArgumentParser(prog='selectionsort.py', description='selection sort program sorts array of given length')
    parser.add_argument('-n', dest='len', type=int, help='integer has to be provided', required=True)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_args()
    arr = genarr(args.len)
    print("Array before sorting of length ", len(arr))
    print(arr)
    print("Array after sorting")
    print(ssort(arr) 
    sys.exit(0)
