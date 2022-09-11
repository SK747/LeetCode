class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # I guess the best way to do this is to use hashmaps
        # hashdicts store the letter and the number of times it occurs
        # First we store all the letters from magazine in a hashmap
        # Then we iterate through magazine and check if the letters are in the dict
        # The only issue is that we cant just use keys I guess because the keys will still exist if the value becomes zero...
        # So this might not be the most efficient solution since we will either have to delete the key
        # Or check if its greater than zero (O(1) but it looks messy)
        hashdict = {}
        for i in range(len(magazine)):
            hashdict[magazine[i]] = 1 + hashdict.get(magazine[i],0)
        
        for j in range(len(ransomNote)):
            if ransomNote[j] in hashdict and hashdict[ransomNote[j]] > 0:
                hashdict[ransomNote[j]] -= 1
            else:
                return False
        return True

r = 'heldl'
m = 'hello'
s = Solution()
print(s.canConstruct(r,m))
