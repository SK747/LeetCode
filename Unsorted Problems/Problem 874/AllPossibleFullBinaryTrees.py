# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        trees = defaultdict(list)
        trees[1].append(TreeNode(0, None, None))
        i = 3
        while i <= n:
            for j in range(1, i, 2):
                left = j
                right = i - 1 - j
                for left_node in trees[left]:
                    for right_node in trees[right]:
                        root = TreeNode(0, None, None)
                        root.left = left_node
                        root.right = right_node
                        trees[i].append(root)
            i += 2
        return trees[n]
            