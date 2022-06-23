#!/usr/bin/env python3

'''
Given a list of integers and a number k, find the kth largest integer in the list. The integer will be stored in the kth_max variable.
'''

def kthmax( arr, k):
    for i in range(k):
        max = arr[i]
        index = i
        for j in range(i+1, len(arr)):
            if arr[j] > max:
                max = arr[j]
                index = j
        if index != i:
           arr[i], arr[index] = arr[index], arr[i]
    return arr[k-1]


if __name__ == '__main__':
    print(kthmax([40,35,82,14,22,66,53], 2))
