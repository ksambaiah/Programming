#!/usr/bin/env python3

def func1(args1, args2):
    args = list((set(args1) - set(args2)))  + list((set(args2) - set(args1)))
    print(args)
func1([1,2,3,10,11], [10,11,12,1])
