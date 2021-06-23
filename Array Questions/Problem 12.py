"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array."""


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0
    count = 0
    print(len(nums))
    while i < len(nums):
        if nums[i] == 0:
            nums.pop(i)
            count = count + 1
        else:
            i = i + 1
    for i in range(count):
        nums.append(0)
    print(count)
    return nums

nums = [0,1,0,3,12]

print(moveZeroes(nums))