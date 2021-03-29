"Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order."

""" Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121] """

def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    numssq = []
    for i in range(len(nums)):
        numssq.append((nums[i])**2)
    numssq.sort()
    return numssq

inp = [-12,345,2,6,7896]

print(sortedSquares(inp))


