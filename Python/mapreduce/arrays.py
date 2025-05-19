#!/usr/bin/env

# Let us write four examples of working with arrays

def addx(i,arr):
    arr1 = []
    for elm in arr:
        arr1.append(elm + i)
    return arr1 

def muly(i, arr):
    arr1 = [] 
    for elm in arr:
        arr1.append(elm * i)
    return arr1 

def fu(x):
    return x+90000

if __name__ == "__main__":
    arr = [3,4,-2,-100,2,3,4]
    print("My array for work is ", arr)
    print("calling addx to add x to each element of the arry")
    print(addx(4,arr))
    print("calling muly to multiply y to each element of the arry")
    print(muly(4,arr))
        
    print("We have same pattern. Function (add or multiply or something) and apply to each element")
    print("Take function apply to each elment is called map")
    print(list(map(fu, arr)))
 
    print("What does map function do? It applies function to each element of the array")
