#!/usr/bin/env python3

# map/reduce/filter functions
def add100(x):
    return x + 100
    
if __name__ == "__main__":
   # populate list with some values
   a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
   
   # filterout even numbers
   b = list(filter(lambda x : x % 2 == 0, a))
   print("Original Array")
   print(a)
   print("filter out even numbers ")
   print(b)
