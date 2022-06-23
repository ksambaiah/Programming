#!/usr/bin/env python3

class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        for i in range(len(nums)-k+1):
            for j in range(i+1, i+k+1): 
                if j < len(nums) and  nums[i] == nums[j]:
                     return True
        return False


if __name__ == "__main__":
    obj = Solution
    print(obj.containsNearbyDuplicate(obj, [99,99], 2))
    print(obj.containsNearbyDuplicate(obj, [1,2,3,1,2,3], 2))
    print(obj.containsNearbyDuplicate(obj, [1,2,3,1], 3))
