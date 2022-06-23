#!/usr/bin/env python3

''' find peak of array what is peak?
  if a[0] >= a[1] for i in 1, len(arry) is peak if a[i] >= a[i-1] and a[i] >= a[i+1] '''


def findPeak(arr):
    b = []
    for i in range(len(arr)-1):
        if i == 0 and arr[i] >= arr[i+1]:
           b.append(arr[i]) 
        elif i == -1 and arr[i] >= arr[i-1]:
           b.append(arr[i]) 
        elif arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
           b.append(arr[i])
    return b
        

if __name__ == "__main__":
    print(findPeak([1,20,2,3,4,10,15,4,400,200,300,900])) 
