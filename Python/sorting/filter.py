#!/usr/bin/env python3

# What does filter do? 

arr = [3, 4, 5, 6, 10, -2, -3, -100, 7]

print("My arr is ", arr)
# Filter all elements greater than 4

print("Mathematics it is called list comprehension")

arr1 =  [ x for x in arr if x >= 4]

print("Elements greater than 4 is ", arr1)

# We can use another way also using filter function.
# What is filter?

arr = [1, 0, -2, -33, 3, 4, 5, 6, 10, -2, -3, -100, 7]
def greatern(num):
    if  num >= 0:
        return True
    return False

arr1 = filter(greatern, arr)
print(list(arr1))
