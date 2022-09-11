# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def isbadversion(self, x):
        arr = [False, False, False, False, False, False, False, True, True, True, True]
        return (arr[x])

    def firstBadVersion(self, n):
        # So this is similar to a binary search I guess
        # The fastest way definitely to start in the middle and then go up or down depending on true or false, dividing by half each time
        # The problem is that if we want to check the next 
        print('hi')
        if self.isbadversion(0):
            return 0
        m = n // 2
        low = 0
        while (n - low > 1) or (m < n -1 ) or m > 1:
            if not self.isbadversion(m):
                if self.isbadversion(m+1):
                    return (m+1)
                else: # otherwise we are at false, and need to move to the remaining half of the array
                    low = m
                    m = (n - low)//2 + m
            if self.isbadversion(m):
                if not self.isbadversion(m-1):
                    return m
                else: # otherwise we are at false, and need to move to the remaining half of the array
                    n = m
                    m = (n - low)//2
            print(n,low,m)



s = Solution()
print(s.firstBadVersion(11))