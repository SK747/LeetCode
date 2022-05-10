 
##    Date: December 20th 2018

 ##   Leetcode Q. 237
    
 ##   Python Solution to merging deleting a node from a linked list

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next