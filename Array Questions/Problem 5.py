""" Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2. """

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    i2 = 0
    z = n + m
    print(z)
    for i in range(len(nums1)):
        print(i)
        if (n == 0 and m > 0):
            m = m - 1
            print("case1")
        elif (m == 0 and n > 0):
            nums1.insert(i, nums2[i2]) ## Python has an insert function that automates the shifting you do in C
            nums1.pop()
            i2 = i2 + 1
            n = n - 1
            print("case2")
        elif (nums1[i] <= nums2[i2]) and m > 0:
            m = m - 1
            print("case3")
        elif (nums1[i] > nums2[i2]) and n > 0:
            nums1.insert(i, nums2[i2])
            nums1.pop()
            i2 = i2 + 1
            n = n - 1
            print("case4")
        else:
            del nums1[1:] # delete multiple elements from list at position 1 to 2
            ## note that nums[:1] does not seem to work in functions
        
nums1 = [2,0]
nums2 = [1]

merge(nums1,1,nums2,0)

print(nums1)


        