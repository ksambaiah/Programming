#!/usr/bin/env python

#Given an array of integers, return indices of the two numbers such 
#that they add up to a specific target.

#You may assume that each input would have exactly one solution, 
#and you may not use the same element twice.

if __name__ == "__main__":
   a = [2,3,4,19,29,44,49,5,14]
   target = 16
   switch = 0
   for x in range(0, len(a)):
       for y in range(1, len(a)):
           if ( (a[x]+a[y]) == target ):
              switch = 1
              break
       if switch:
          break
   print("matches are %d, %d, %d" %(x, y, target))
