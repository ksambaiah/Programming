#!/usr/bin/env python3

def bsearch1(arr, lo, high, num):
    if high >= lo:
       middle = high-lo // 2
       if arr[lo+middle] == num:
          return lo+middle
       elif arr[lo+middle] < num:
          return bsearch1(arr, lo+middle+1, high, num) 
       else:
          return bsearch1(arr, lo, lo+middle-1, num)
    return -1

if  __name__ == '__main__':
    arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
    value = bsearch1(arr,0,len(arr)-1, 11)
    print(value)
