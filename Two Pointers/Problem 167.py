"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] 
and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
"""

## Using two pointers, we can have one start from the start and one from the end
## Since they are already sorted, this is quite effective
## 6 minute solution. 85% speed, 90% memory.

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i,j = 0,len(numbers)-1
        while j >= i:
            result = (numbers[j] + numbers[i])
            if result == target:
                return [i+1,j+1]
            elif result > target:
                j -= 1
            elif result < target:
                i += 1
        print('no answer found')

s = Solution()
nums = [1,2,3,4,5]
print(s.twoSum(nums,7))
