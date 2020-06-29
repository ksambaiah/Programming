#!/usr/bin/env python3

# List comprehension is fun

if __name__ == "__main__":
   # populate list with some values
   a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
   # Get all even elements
   even = [i for i in a if i % 2 == 0]
   print(a)
   print("Even numbers in the above list")
   print(even)
   mod3 = [i for i in a if i % 3 == 0]
   print("Divisible by three numbers in the above list")
   print(mod3)
