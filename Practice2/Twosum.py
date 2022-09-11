# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Guaranteed only one solution



class Solution(object):

    # Obviously an O(n^2 solution is very easy
    def twoSum1(self, nums, target):
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                print(nums[i],nums[j])
                if nums[j] == target - nums[i]:
                    return [i,j]

    # But the O(n) solution requires a hashmap
    # Obviously we can just store each number in memory as we go on.
    # CHECKING A HASHMAP IS A O(1) OPERATION
    # We need a dict, not a set, because we also need the index...

    def twoSum2(self,nums,target):
        hashdict = {}
        for i in range(len(nums)):
            z = target - nums[i]
            if z in hashdict:
                return[hashdict[z],i]
            else:
                hashdict[nums[i]] = i
            


s = Solution()
nums = [1,2,3,5,7]
print(s.twoSum2(nums,7))
