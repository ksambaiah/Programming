#!/usr/bin/env python
import random

def selectionSort(a):
    for i in range(1, len(a)):
        swap = 0
        pivot = a[i]
        for j in range(i-1, -1, -1):
            if pivot < a[j]:
               a[j+1] = a[j]
               if (j == 0):
                   a[j] = pivot
                   break
            else:
               a[j+1] = pivot
               break
    return a
         

if __name__ == "__main__": 
   size = 50
   #Generate list of size elements
   randomList = random.sample(range(0, 9900), size)
   print(randomList)
   sortedList = selectionSort(randomList)
   print(sortedList)
