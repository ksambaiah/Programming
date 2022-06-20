#!/usr/bin/env python3

class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        def helper(start, end, ls):
            if start >= end:
                return
        
            # swap the first and last element
            ls[start], ls[end] = ls[end], ls[start]        

            return helper(start+1, end-1, ls)
    
        helper(0, len(s)-1, s)
        print(s)

if __name__ == "__main__":
    obj = Solution
    t = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    obj.reverseString(obj,t)
