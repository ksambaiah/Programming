#!/usr/bin/env python3

''' This does merge which is needed in merge sort '''

def merge(arr, b, s, f):
    for i in range(s+1, f+1):
        key = arr[i]
        j = i - 1
        while key < arr[j]  and j >= b:
           arr[j+1] = arr[j]
           j = j - 1 
        arr[j+1] = key
    return arr

if __name__  == "__main__":
    print(merge([0,1,2,3,4,5,100,200,-20,2,10,20,30,40], 0, 7, 13))
