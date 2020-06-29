#!/usr/bin/env python3

# map/reduce/filter functions
def add100(x):
    return x + 100
    
if __name__ == "__main__":
   # populate list with some values
   a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
   
   # add 100 for each element
   b = list(map(add100, a))
   print("Original Array")
   print(a)
   print("add100 function using map ")
   print(b)
