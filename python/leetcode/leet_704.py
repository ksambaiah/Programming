#!/usr/bin/env python3
'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)

        # Binary Search
        while start < end:
            mid = ((end-start) // 2) + start
            # Mid point is target
            if nums[mid] == target:
                return mid
            # Mid point bigger than target
            elif nums[mid] > target:
                end = mid
            # Mid point smaller than target
            elif nums[mid] < target:
                start = mid+1

        return -1
    print(search([1,2,3,4,5,6,7,8,9], 10))
        
