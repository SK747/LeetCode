# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.$

from itertools import count


class Solution(object):
    def maxSubArray(self, nums):
        high = nums[0]
        count = 0
        # The O(n) algorithm for this is not that tricky
        # We will only be iterating once. 
        # The trick is that negative additions can literally be completely ignored
        
        for i in range(len(nums)):
            if count <= 0:
                count = nums[i]
            else:
                count = count + nums[i]
            if count > high:
                high = count
        return high
        
            
            


s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))
