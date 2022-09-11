class Solution(object):
    def search(self, nums, target):
        mid = len(nums) // 2
        high = len(nums)
        low = 0
        while high-low > 1:
            if nums[mid] < target:
                low = mid
                mid = (high-low)//2 + mid
            if nums[mid] > target:
                high = mid
                mid = (high-low)//2
            if nums[mid] == target:
                return True
            print(high,mid,low)
            print(nums[mid])
        return False

                



s = Solution()
j = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18]
print(s.search(j,9))