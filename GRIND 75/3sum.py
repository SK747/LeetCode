class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        print(nums)
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i-1]:
                i = i + 1
            else:
                l = i+1
                r = len(nums)-1
                print('once')
                while l < r:
                    print(nums[i],nums[l],nums[r])
                    if nums[l] + nums[r] + nums[i] == 0:
                        res.append([nums[l],nums[r],nums[i]])
                        l += 1
                        r -= 1
                    if nums[l] + nums[r] + nums[i] > 0:
                        while r > l:
                            r -= 1
                            if nums[r] != nums[r+1]:
                                break
                    if nums[l] + nums[r] + nums[i] < 0:
                        while l < r:
                            l += 1
                            if nums[l] != nums[l-1]:
                                break
                i = i + 1
        return res

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))