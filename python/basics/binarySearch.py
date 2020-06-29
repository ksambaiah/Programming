#!/usr/bin/env python

import random

# Generate random list of integers amounting 1000 
def intArray(size):
    step = 1
    arr = []
    arr.append(100)
    for i in range(1, size):
        arr.append(random.randint(arr[i-1], arr[i-1]+step))
    return arr

def binarySearch(arr, ele, i, j):
    middle = int((j-i)/2) + i
    if j >= i:
        if arr[middle] == ele:
           return middle
        elif arr[middle] < ele:
           return binarySearch(arr, ele, middle+1, j)
        elif arr[middle] > ele:
           return binarySearch(arr, ele, i, middle-1)
    else:
        return -1
if __name__ == "__main__": 
   size = 30000 
   intArray(size) 
   sortedArray = intArray(size) 
   # Geneerate random set of sorted array Array
   ele = random.randint(sortedArray[0], sortedArray[-1])
   ele = 999
   match = binarySearch(sortedArray, ele, 0, len(sortedArray)-1)
   if match == -1:
      print("Element % d is not in the array" %(ele))
   else:
      print("Element % d is in the list % d" %(ele, match))
  
