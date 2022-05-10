class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        templist = ''
        longest = 0
        for j in range(len(s)):
            for i in range(j,len(s)):
                if s[i] in templist:
                    if len(templist) >= longest:
                        longest = len(templist)
                    templist = s[i]
                else:
                    templist=templist + s[i]
                print(templist)
            print('first loop done')
            if len(templist) >= longest:
                longest = len(templist)
            templist = ''
        return longest
        

s = Solution()
input = "qrsvbspk"
print(s.lengthOfLongestSubstring(input))