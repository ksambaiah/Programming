#!/usr/bin/env python
import random

# Take first element, get elements lower than that
# Elements higher than it and repeat it

def quickSort(a):
    if (len(a)) <= 1:
       return a
    higher  = [i for i in a[1:] if i > a[0]] 
    lower   = [i for i in a[1:] if i <= a[0]] 
    return quickSort(lower) + [a[0]] + quickSort(higher)
   

if __name__ == "__main__": 
   size = 50
   #Generate list of size elements
   randomList = random.sample(range(0, 999), size)
   print(randomList)
   sortedList = quickSort(randomList)
   print(sortedList)
