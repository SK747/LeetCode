""" Given an array nums of integers, return how many of them contain an even number of digits."""

def findNumbers(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    z = 0
    for i in range(len(nums)):
        x = nums[i]
        y = 0
        print(x)
        while x >= 1:
            x = x / 10
            y += 1
        print(y)
        if (y%2) == 0:
            z += 1
    return z

inp = [12,345,2,6,7896]

print(findNumbers(inp))
