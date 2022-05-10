class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]

s = Solution()
input = [1,2,3,4,5,6,7]
print(s.twoSum(input, 9))