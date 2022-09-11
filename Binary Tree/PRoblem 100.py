# Find same tree
# Easy question
# We will just recursively check 



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        # The recursive case
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

        # note we can just keep going until we reach a point where p and q are true because the nodes are empty
        # at this point we know the trees are the same
        # So we only check for the false

        