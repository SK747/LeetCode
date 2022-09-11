class Solution(object):
    def isAnagram(self, s, t):
        # Firstly, if they arent the same length, then they aren't anagrams
        if len(s) != len(t):
            return False
        
        # Now, we are going to use a hashmap to do this
        # in the hashmaps we will store the letters as keys, and store the number of times it occurs as the value
        hashdict1 = {}
        hashdict2 = {}
        for i in range(len(s)):
            # hashdict1[s[i]] = hashdict1[s[i]] + 1 ----- YES but this will run into an error if it doesnt exist. So we can use get
            hashdict1[s[i]] = 1 + hashdict1.get(s[i],0)
            hashdict2[t[i]] = 1 + hashdict2.get(t[i],0)

        return (hashdict1 == hashdict2)

s = Solution()
print(s.isAnagram('hey','yhe'))


