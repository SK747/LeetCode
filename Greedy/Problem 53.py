# This is leetcode hard but its actually really easy
#  nums = [-2,1,-3,4,-1,2,1,-5,4]
# We want to output 6 which is the largest contiguous array
# We will merely iterate over the array once. 
# If our sum is negative WHEN WE REACH A POSITIVE, then we can discard the negative portion and start from the positive number
# I suppose this is the greedy algorithm SORTOF?

class Solution(object):
    def maxSubArray(self, nums):
        maxsub = nums[0] # IMPORTANT: this is done because initializing to zero doesn't make sense as the highest could be negative

        total = 0

        for i in range(len(nums)):
            if total < 0:
                total = nums[i]
            else:
                total = total + nums[i]
            if total > maxsub:
                maxsub = total
            print(total,maxsub)
        return maxsub


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))



        