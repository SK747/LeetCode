class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # Okay well, if it is zero, then we just keep it as zero
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    mat[i][j] = 2
        return mat


mat = [[0,0,0],[0,1,0],[0,0,0]]
s = Solution()
print(s.updateMatrix(mat))
        