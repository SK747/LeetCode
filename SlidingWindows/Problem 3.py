class Solution(object):
    def lengthOfLongestSubstring(self, str):
        hashset = set()
        if len(str) == 0:
            return 0
        if len(str) == 1:
            return 1
        
        l,r = 0,1
        count = 1
        maxcount = 1
        hashset.add(str[l])
        while r < len(str):
            print('l and r are,', l,r)
            print('rl and rr are,', str[l],str[r])
            if str[r] in hashset:
                print('first loop')
                while str[l] != str[r]:
                    print('in the second while loop, we are about to remove', str[l], 'but r is', str[r])
                    hashset.remove(str[l])
                    count -= 1
                    l += 1
                
                l += 1
                r += 1
            elif str[r] not in hashset:
                print('second loop')
                hashset.add(str[r])
                r += 1
                count += 1
                print('count is', count)
                if count > maxcount:
                    maxcount = count
            
            print(hashset)
        return maxcount
            

s = Solution()
str = 'abcabcbb'

print(s.lengthOfLongestSubstring(str))
