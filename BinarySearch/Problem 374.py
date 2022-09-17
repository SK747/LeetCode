# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):
class Solution(object):
    def guessNumber(self, g, n):
        """
        :type n: int
        :rtype: int
        """
        # we can obviously just use binary search
        lo, hi = 0, n
        while lo <= hi:
            mid = (hi + lo)//2
            if mid >= g:
                hi = mid - 1
            if mid < g:
                lo = mid + 1
            if mid == g:
                return mid
        return hi


s = Solution()
print(s.guessNumber(3,12))