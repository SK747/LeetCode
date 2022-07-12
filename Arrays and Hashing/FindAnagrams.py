## write a function that determines for each pair if it’s an anagram or not
## for each pair of words your function will print to standard output (stdout) 
# the value 1 if the pair is an anagram or 0 otherwise (one result per line)

class Solution:
    def DetermineAnagrams(self, arr1, arr2):
        countS, countT = {},{} 
        retarr = []
        for i in range(len(arr1)):
            if len(arr1[i]) != len(arr2[i]):
                retarr.append(0)
            for j in range(len(arr1[i])):
                print(arr1[i][j])
                countS[arr1[i][j]] = 1+countS.get(arr1[i][j],0) ## THE GET IS FOR THE CASE THAT CountS is NOT INTIIALIZED
                countT[arr2[i][j]] = 1+countT.get(arr2[i][j],0)
            for k in range(len(arr1)):
                print(countS[arr1[i][k]],countT[arr2[i][k]])
                if countS[arr1[i][k]] != countT[arr2[i][k]]:
                    retarr.append(0)
                    break
                else:
                    retarr.append(1)
                    break
        return retarr

s = Solution()
arr1 = ['ey','yo']
arr2 = ['ye','gh']
print(s.DetermineAnagrams(arr1,arr2))
        
