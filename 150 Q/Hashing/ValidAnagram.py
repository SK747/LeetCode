## Again we use hashmaps
## This time we need to use it as a dict
## 4 minutes

def ValidAnagram(s,t):
    hashdict1 = {}
    hashdict2 = {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        hashdict1[s[i]] = 1 + hashdict1.get(s[i],0)
        hashdict2[t[i]] = 1 + hashdict2.get(t[i],0)
    return hashdict1 == hashdict2

print(ValidAnagram('hello','olelh'))