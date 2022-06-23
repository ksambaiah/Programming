#!/usr/bin/env python3

''' binary search algorithm '''


def bsearch(arr, s, e, k):
    mid =  s + (e - s ) // 2
    if  s == e and arr[s] != k:
       return -1
    if arr[mid] == k:
       return mid
    elif arr[mid] < k:
       return bsearch(arr, mid+1, e, k)
    elif arr[mid] > k:
       return bsearch(arr, s, mid-1, k)

if __name__ ==  "__main__":
    print(bsearch([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], 0, 18, 10))
    print(bsearch([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], 0, 18, 9))
    print(bsearch([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], 0, 18, -100))
    print(bsearch([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], 0, 18, 100))
    print(bsearch([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], 0, 18, 18))
