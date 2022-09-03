# Again we are going to use recursion for this
# Need to find max depth
# we can use the max function which will just compare the two values and spit out the higher one
# We can recursively search through using DFS


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        # Edge case
        if not root:
            return 0
        
        # DFS
        return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))