#!/usr/bin/env python
import random

def selectionSort(a):
    for i in range(0, len(a)):
        swap = 0
        min = a[i]
        index = i
        for j in range(i+1, len(a)):
           if a[j] < a[i]:
               min = a[j]
               index = j
               swap = 1
        if swap:
           a[index] = a[i]
           a[i] = min
    return a
         

if __name__ == "__main__": 
   size = 20
   #Generate list of size elements
   randomList = random.sample(range(-999990, 999999), size)
   print(randomList)
   sortedList = selectionSort(randomList)
   print(sortedList)
