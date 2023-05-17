class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        palarray = []
        while x > 0:
            palarray.append(x%2)
            x = x//10
            print(palarray,x)
        print('I have left the ')
        l, r = 0, len(palarray)-1
        while l < r:
            if palarray[l] != palarray[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

s = Solution()

print(s.isPalindrome(121))

