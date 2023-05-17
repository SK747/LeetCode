class Solution(object):
    def updateMatrix(self, mat):
        ## Top and left
        for row in range(len(mat)):
            for col in range(len(mat)):
                if mat[row][col] == 0:
                    continue
                else:
                    x = mat[row-1][col] if row > 0 else float('inf')
                    y = mat[row][col-1] if col > 0 else float('inf')
                    mat[row][col] = min(x,y)+1
        
        for row in range(len(mat)-1,-1,-1):
            for col in range(len(mat)-1,-1,-1):
                if mat[row][col] == 0:
                    continue
                else:
                    a = mat[row+1][col] if row < len(mat)-1 else float('inf')
                    b = mat[row][col+1] if col < len(mat[col])-1 else float('inf')
                    mat[row][col] = min(mat[row][col],min(a,b)+1)
        
        return mat

s = Solution()
print(s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))