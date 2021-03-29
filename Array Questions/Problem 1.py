""" Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000 """

"ALGORITHM: Simply iterate through and have a counter..."


def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    maxcount = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            if count > maxcount:
                maxcount = count
            count = 0
    if count > maxcount:
            maxcount = count
            count = 0
    return maxcount    


inp = [1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0]

print(findMaxConsecutiveOnes(inp))
