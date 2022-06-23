#!/usr/bin/env python3


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
           return n
        p, q = 1, 2
        for i in range(3, n+1):
            p, q  = q, p+q          
        return q

if __name__ == "__main__":
    obj = Solution
    print(obj.climbStairs(obj, 5))
            

