class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        bi = len(nums)-1 #backindex
        index = bi

        for i in range(len(nums)):
            if nums[i] == val:
                while True:
                    if nums[bi] == val and bi >= 0:
                        bi = bi - 1
                    else:
                        break
                if i >= bi:
                    break
                nums[i], nums[bi] = nums[bi], nums[i]
        del nums[len(nums)-(index - bi):]
        return len(nums)