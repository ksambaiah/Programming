#!/usr/bin/env python

# Given a sorted array nums, remove the duplicates in-place such 
# that each element appear only once and return the new length.

# [1,2,3,4,4,4,5,5,6,7,8] given new array should be
#[1,2,3,4,5,6,7,8] and return 8

if __name__ == "__main__":
   array = [1,2,3,4,4,4,5,5,6,7,8]
   # Set Datastructure in python will not have duplicates
   # Set in maths will not have duplicates
   setA = set(array)
   print("Length of List is % d" %(len(array)))
   print("Length of set from the list construct is % d" %(len(setA)))
