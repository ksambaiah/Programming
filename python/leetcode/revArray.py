#!/usr/bin/env python

# Reverse array in place
# Slicing of Array
def rev(s):
    slength=len(s)
    slicedS = s[slength::-1]
    print(slicedS)

if __name__ == "__main__":
     s = "hello"
     print(s)
     rev(s)
