"""Students are asked to stand in non-decreasing order of heights for an annual photo.
Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.
Notice that when a group of students is selected they can reorder in any possible way between themselves and the non selected students remain on their seats."""


def heightChecker(heights):
    
    """
    :type heights: List[int]
    :rtype: int
    """

    sortedheights = sorted(heights)
    k = 0
    l = 0
    for i in range(len(heights)):
        l = sortedheights.index(heights[i])
        k = k + abs(l-i)
        if heights[i] == heights[i-1]:
            k = k - 1
    return k

nums = [1,2,2,3,4,4,4]
print(heightChecker(nums))