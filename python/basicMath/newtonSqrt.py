#!/usr/bin/env python
#Compute Squareroot using Newton method

def improve(g, n):
    return (g+n/g)/2

def notgoodEnough(g, n, e):
    if (abs(n-(g*g))) > e:
       return 1
    else:
        return 0

def sqrtCompute(g, n, e):
    r = notgoodEnough(g,n,e)
    while r:
       r = notgoodEnough(g,n,e)
       g = improve(g, n)
    return g 

if __name__ == "__main__":
    guess=1.0
    number=22.0
    epsilon=0.00000001
    sqrt = sqrtCompute(guess, number,epsilon)
    print("Squareroot of %d is %10f" %(number, sqrt))
     
