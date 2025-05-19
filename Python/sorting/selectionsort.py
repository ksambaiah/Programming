#!/usr/bin/env python3
import random
import sys
import argparse
import unittest

"""
selection sort n^{2} algorithm
We are using argparse module to pass arguments
We are using sys module for exit status
unittest module for test cases


"""


def genarr(n):
    arr = []
    for i in range(n):
       num = random.randint(-9999991999, 9999999999)
       arr.append(num)
    return arr

def ssort(arr):
    """ Selection sort is basic sorting type """
    size = len(arr) 
    for i in range(0, size):
       index = i
       for j in range(i+1, size):
           if arr[index] > arr[j]:
              index = j
       if i != index:
           (arr[i], arr[index]) = (arr[index], arr[i])
    return arr

# Take array and test arr[i] <= arr[i+1]] srarting i 0 to n-1
def is_sorted_ascending(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

class TestArraySorted(unittest.TestCase):
    def __init__(self, arr):
      self.arr = arr
    def test_sorted_array(self):
        self.assertTrue(is_sorted_ascending(self.arr))

    def test_unsorted_array(arr):
        self.assertFalse(is_sorted_ascending(self.arr))

def get_args():
    parser = argparse.ArgumentParser(prog='selectionsort.py', description='selection sort program sorts array of given length')
    parser.add_argument('-n', dest='len', type=int, help='integer has to be provided', required=True)
    parser.add_argument('-t', dest='test',  help='testing if array sorted')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_args()
    arr = genarr(args.len)
    print("Array before sorting of length ", len(arr))
    print(arr)
    print("Array after sorting")
    print(ssort(arr)) 
    if args.test and (is_sorted_ascending(arr) is True):
        print("Array is in sorted order")
          
    sys.exit(0)
