class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        for i in range(len(arr)):
            next = arr[i+1]
            if next < arr[i]:
                return i

s = Solution()
arr = [0,1,0]
print(s.peakIndexInMountainArray(arr))