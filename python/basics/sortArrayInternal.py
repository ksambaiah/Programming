#!/usr/bin/env python
import random

if __name__ == "__main__": 
   size = 1000
   #Generate list of size elements
   randomList = random.sample(range(0, 9999), size)
   randomList.sort()
   print(randomList)   
