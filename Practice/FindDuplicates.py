class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        ## So we'll solve this using a hashmap
        ## Normally we'd have to run through every number and then for every number we'd need to check the array again
        ## Thats basically O(n^2) time although I guess its O(nlogn) if you do it properly
        ## But with a hashmap you can just put them into a set
        hashmap = set() ## In this case our hashmap will just be an set that stores only one of each number
        ## And then check if a number is already in the set
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            else:
                hashmap.add(nums[i])
        return False

    def containsDuplicate2(self, nums:list[int]) -> bool:
        nums2 = set(nums)
        return len(nums2) == len(nums)
        

s = Solution()
arr1 = [1,2,3,4]

print(s.containsDuplicate(arr1))