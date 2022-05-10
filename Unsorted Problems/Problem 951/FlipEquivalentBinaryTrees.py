# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1, root2) -> bool:
        
        def flip(t1, t2):
            if (t1, t2) == (None, None):
                return True
            elif t1 == None and t2 is not None:
                return False
            elif t1 is not None and t2 is None:
                return False
            elif t1.val != t2.val:
                return False
            
            return (flip(t1.left, t2.left) and flip(t1.right, t2.right)) or (flip(t1.left, t2.right) and flip(t1.right, t2.left))
        
        return flip(root1, root2)