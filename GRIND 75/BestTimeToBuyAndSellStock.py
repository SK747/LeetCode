class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l,r = 0,0
        maxs = 0
        hashset = set()
        while r < len(s):
            if s[r] not in hashset:
                hashset.add(s[i])
            


        return maxs

h = {1,2,3}
h.remove(2)
print(h)

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))