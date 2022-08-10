class Solution(object):
    ## Alright so we CANNOT USE sorted here because sorted is O(n log n)
    ## But apparently set is O(n)
    ## So I guess we can start by converting it into a set and that will allow us to solve this problem...
    ## And... that lets us solve this problem rather easily
    def longestConsecutive(self, nums):
        nums = set(nums)
        print(nums)
        count = 0
        maxcount = 0
        for i in range(len(nums)-2):
            if (nums[i+1]-nums[i])==1:
                count = count + 1
                if count > maxcount:
                    maxcount = count
            else:
                count = 0
        return maxcount
    ## okay so SETS ARE NOT SUBSCRIPTABLE. Lets ignore that for now. 
    ## HOWEVER. YOU CAN STILL USE SETS TO LOOK UP WITH O{1) COMPLEXITY
    ## THAT IS THE HOW YOU SHOULD USE HASHMAPS
    def longestConsecutive(self, nums):
        hashmap = set(nums)
        length = 0
        maxlength = 0
        for i in range(len(nums)):
            if (nums[i]-1) not in hashmap:
                while (nums[i]+length) in hashmap:
                    length = length + 1
                if length > maxlength:
                    maxlength = length
        return maxlength





s = Solution()
test = [1,2,3,4,6,9,4,0]
print(s.longestConsecutive(test))
