#!/usr/bin/env python

#Given a sorted array and a target value, return the index 
#if the target is found. If not, return the index where it 
#would be if it were inserted in order.

if __name__ == "__main__":
   # Given array
   a = [1,2,7,8,10,12,15,100]
   pivot = -77
   i = 0
   for x in a:
      if x > pivot:
         break
      i = i+1
   print("Position where we can add element is % d" %(i))
   
       
