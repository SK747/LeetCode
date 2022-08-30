# so basically given something like
# this Input: head = [1,3,4] 2 = [1,2,5]
# Output [1,1,2,3,4,5]
# Both are sorted
# So we have two heads. First thing is to compare the two
# The lower of the two should then look at the next in its list
# If that is higher, then that link should be broken (after storing the pointer in a temp) - actually not the case since we are outputting a new list
# The new link should then be made from the lower head to the higher head
# If that is lower, then the lower head should move to the next

# The only other thing to note is that we need to output a new linked list
# For this we have an edge case because if we want to insert an element into this new list we need to have a node there already
# We can use a dummy node for this




class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next


            