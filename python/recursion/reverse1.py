#!/usr/bin/env python3

def reverse (s):
    s = list(s)
    m = len(s)
    for i in range ( m // 2):
        r = s[i]
        s[i] = s[m-i-1] 
        s[m-i-1] = r
    s = ''.join(s)
    return s

if __name__ == "__main__":
    print(reverse("abcdefg")) 
    print(reverse("Sambaiah Kilaru")) 
