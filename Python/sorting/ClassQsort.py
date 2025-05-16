#!/usr/bin/env python3
import random
import sys

"""
Quick sort as name suggest fastest start with O(nlog(n)) time it finishes sorting on average

How it works? Take a pivotal element normally first element, sort elements smaller than it to left
and bigger than it to other side  and repeat it. 

"""

class Qsort:
   def __init__(self, arr):
      self.arr = arr

   def partition(self, start, end):
       pivot = self.arr[end]
       i = start - 1
       for j in range(start, end):
           if self.arr[j] <= pivot:
              i = i+1
              (self.arr[i], self.arr[j]) = (self.arr[j], self.arr[i])
       (self.arr[i+1], self.arr[end]) = (self.arr[end], self.arr[i+1])
       return i+1

   def sort(self, start, end):
       if start < end:
          r = self.partition(start, end)
          self.sort(start, r-1)
          self.sort(r+1, end)

class RandomArr:
   def __init__(self, n):
      self.arr = n
   def genarr(n):
       arr = []
       for i in range(n):
          num = random.randint(-9999991999, 9999999999)
          arr.append(num)
       return arr


if __name__ == "__main__":
    if len(sys.argv) != 2:
       print("usage: sys.argv[0] num  num is the number of elements to sort out")
       # Exit the program
       sys.exit(100)
    if not isinstance(int(sys.argv[1]), int):
       print("Usage sys.argv[0] num num must be of integer type")
       sys.exit(101)
    #arr = genarr(int(sys.argv[1]))
    arr = RandomArr.genarr((int(sys.argv[1])))
    print(arr)
    print(Qsort.sort(arr, 0, len(arr)-1)) 
    sys.exit(0)
