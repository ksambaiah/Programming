#!/usr/bin/env python3
# Simple ways to access elements in array
arr = [1,100,35,678,234,-90,87,"asdf","apple"]
for i in range(0,len(arr)):
    print(arr[i])
for x in arr:
    print(x)
print(arr[7])
print(arr[-2])
# Slice of an array

b = arr[2:]
print(b)
