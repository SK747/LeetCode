""" Given an array, find the area with max water (no larger 'containers) within

Strategy: 
This is quite easy. Have one pointer pointing at the start of the array and another at the end.
The container then contains the lower of the two pointer magnitudes multiplied by the distance between pointers + 1
We then move the SMALLER of the two pointers
We STOP when the distance * the larger of the two pointers cant possibly be higher than the max number we've found

Runtime: 775 ms, faster than 85.59% of Python3 online submissions for Container With Most Water.
Memory Usage: 27.5 MB, less than 57.49% of Python3 online submissions for Container With Most Water.
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max = 0
        i = 0
        j = len(height)-1
        while i <= j:
            container = (j-i)*(min(height[i],height[j]))
            print(height[i],height[j])
            print(container)
            if container > max:
                max = container
            if height[i] < height[j]:
                i += 1
            elif height[i] >= height[j]:
                j -= 1
        return max

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
