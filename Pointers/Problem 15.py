"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

## Solution is obviously to use three pointers


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ret = []
        i, j = 0
        k = len(nums)-1
        while i < len(nums):
            print('s')