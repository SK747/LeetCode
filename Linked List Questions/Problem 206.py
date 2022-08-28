# so basically given something like
# this Input: head = [1,2,3,4,5]
# want Output: [5,4,3,2,1]
# How can we do this
# So really its just a matter of understanding basics of linked lists
# Now head points to the start of the linked list. theres no tail i guess
# now with reversing the list the first step is to set what the head points to as the prev, then we'll move the head to self.next
# then we'll reverse the link. We do this with temp variables


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head
        
        while curr: # once curr iterates and sees nothing, we know our linked list is done
            temp = curr.next ## We are about to break this link so we need to store it in a temp variable
            curr.next = prev ## Reverse the link, the first will point to null of course
            prev = curr
            curr = temp
        return prev # Prev is now the head
            
        