

## Date: December 11th 2018

## Leetcode Q.283

## Move zeroes to end of array

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: modify nums in-place. returns nothing
        """
        x = 0
        while(0 in nums):
            nums.remove(0)
            x = x + 1
        while(x!=0):
            nums.append(0)
            x = x - 1