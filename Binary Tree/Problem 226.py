# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# We can use recursion to solve this easily.
# We'll do a depth first search meaning we go to each level and check all nodes before proceeding
# So in this case we'll start at 4, proceed to the next depth and swap the two.
# Then call the algorithm again for each node

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        # Edge case
        if not root:
            return None

        # Start algorithm
        temp = root.left
        root.left = root.right
        root.right = temp

        # Call recursively
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
