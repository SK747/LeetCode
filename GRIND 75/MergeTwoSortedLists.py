# Lets Construct Linked Lists in Python
# This defines a node class 
from multiprocessing.dummy import DummyProcess


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Then the linked list class. This will call the node class some times I guess
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.data, " -> ", end = '') 
            temp = temp.next
        print("")

    def size(self):

        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node= self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_end = Node(data)
        current = self.head

        while current:
            prev = current
            current = current.next
        prev.next = new_end
        new_end.next = None

    def get_next_node (self,node):
        return node.next.data



class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # The algorithm here is quite simple.

        # We need to output a new list, so we need a dummy node to start at null
        dummy = Node()
        tail = dummy
        p = list1.head
        q = list2.head

        # Now we want to iterate over both lists (until we reach the end of one of them)
        # In this case list1 is the entire list, not just the head

        while p and q:
            if p.data <= q.data:
                tail.next = p
                p = p.next
                tail = tail.next
            else:
                tail.next = q
                q = q.next
                tail = tail.next
        
        if p:
            tail.next = p
        if q:
            tail.next = q
        


    
        

        

llist = LinkedList()
llist.head = Node(1)
llist.insert_at_end(2)
llist.insert_at_end(3)
llist.insert_at_end(5)
llist.insert_at_end(6)
llist.printList()

llist2 = LinkedList()
llist2.head = Node(1)
llist2.insert_at_end(3)
llist2.insert_at_end(4)

llist2.printList()

s = Solution()
s.mergeTwoLists(llist, llist2)




    
    

