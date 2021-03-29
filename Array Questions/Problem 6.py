"""Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length."""

## Solution Beats 92.51% in runtime, beats 67% in memory

def removeElement(nums, val):
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
                        print('while')
                        print(val)
                        print(nums[bi])
                        print(bi)
                        bi = bi - 1
                    else:
                        print('help me')
                        break
                if i >= bi:
                    break
                print('if')
                nums[i], nums[bi] = nums[bi], nums[i]
                print(nums)
                print(nums[bi])
        print(bi)
        del nums[len(nums)-(index - bi):]
        return len(nums)

nums = [1]
val = 3

print(removeElement(nums,2))
print(nums)

