#!/usr/bin/env python3

''' insertion sort [1,0,100,-2,-9] '''

def insertionSort(a):
    steps = 0
    for j in range(1, len(a)):
        key = a[j]
        i = j-1
        steps = steps + 1
        while i >=0 and key < a[i]: 
            steps = steps + 1
            a[i+1] = a[i]
            i = i - 1
        a[i+1] = key
    print("total Steps", steps)
    return a


if __name__ == "__main__":
    print(insertionSort([1,-100, -2, -9, 0, 99]))
    print(insertionSort([1,-100, -200, 3]))
    print(insertionSort([1,-100]))
    print(insertionSort([-100, -99, -98,0,1,2,3,4,5,6,7,8,9]))
    print(insertionSort([100, 99, 98,97,96,95,94,93,92,91,90,89,88,87]))
