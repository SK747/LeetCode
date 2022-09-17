class Solution(object):
    def mySqrt(self, x):
        #use a binary search
        print(x)
        low = 0
        high = x
        while low <= high:
            mid = (high+low)//2
            print(low,mid,high)
            if (mid*mid) >= x:
                high = mid-1
            elif mid*mid < x:
                low = mid+1
            else: return mid
        return high

s = Solution()
print(s.mySqrt(8))
