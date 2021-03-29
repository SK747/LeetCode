"""Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory."""

## Simple solution, beats 50% of solutions in runtime, 92% in memory dist

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            print('did this execute')
            nums.pop(i)
        else:
            i = i + 1
        print(nums)
    return len(nums)

nums = [0,0,0,0,0,0]

removeDuplicates(nums)

print(nums)