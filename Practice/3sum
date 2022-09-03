class Solution:
    def twoSum(self, nums, index,retarray):
        hashset = set()
        for i in range(len(nums)):
            if i != index:
                diff = (nums[index] + nums[i])*-1
                if diff in hashset:
                    retarray.append([diff,nums[i],nums[index]])
                else:
                    hashset.add(nums[i])
        return retarray
    def threesum(self, nums: list[int]) -> bool:
        # Okay so you want to send a list of lists back to the caller that has all the combinations of numbers that add up to 0
        retarray = []
        # One confusing thing is how do I send a list of lists back?? 
        # Anyway we're going to use two pointers
        # The solution basically involves one pointer pointing to the first number and then the other pointer solving the two sum problem
        # looking for the two numbers
        # We can basically just add the two sum function here since we will be calling it
        # We want to modify it so it sends us the numbers back
        # But in the original twosum we're guaranteed two numbers. 
        # In this case we can have zero or one or more.
        # Okay now with the twosum done, we can just iterate over the nums array
        # We dont want duplicates so we need to use a hashset
        hashset = set()
        for i in range(len(nums)):
            if nums[i] != hashset:
                self.twoSum(nums,i,retarray)
                hashset.add(nums[i])
        return retarray
    ## Okay this solution still contains duplicates so we need a new solution.
    ## So obviously the solution is that we dont want to iterate over the loop AGAIN.
    ## However this is easier to do just by sorting the array. 
    ## Once we sort the array we just want to make sure that we dont use the same number twice
    ## Then on the remainder of the array. Since it is sorted we can use a two pointer twosum approach.
    def sum2(self, nums,target,arr,l):
        r = len(nums)-1
        while l < r:
            if nums[l]+nums[r] == target:
                arr.append([nums[l],nums[r]])
                l += 1
            if nums[l]+nums[r] > target:
                r -= 1
            if nums[l]+nums[r] < target:
                l += 1
        return arr
    def sum3(self, nums: list[int]) -> bool:
        hashset = set()
        retarray = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums(i) not in hashset:
                retarray = self.sum2(nums,)



        




        
        

s = Solution()
arr1 = [1,2,3,4,0,-4]

print(set(arr1))
