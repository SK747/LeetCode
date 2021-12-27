class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        for i in range(len(arr)):
            next = arr[i+1]
            if next < arr[i]:
                return i

#s = Solution()
#arr = [0,1,0]
#print(s.peakIndexInMountainArray(arr))

# Actual way to solve it should be a binary search
# In this case we have something like True, True, True, False, False
# Therefore its perfect for a binary search
class Solution2:
    
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        i = len(arr)//2
        while i > 1 or i < len(arr)-1:
            if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
                return i
            elif arr[i] > arr[i+1] and arr[i] < arr[i-1]:
                i = i - 1
            elif arr[i] < arr[i+1] and arr[i] > arr[i-1]:
                i = i + 1

s = Solution2()
arr = [0,1,2,0]
print(s.peakIndexInMountainArray(arr))