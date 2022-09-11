# Lets Construct Linked Lists in Python

# This defines a node class 
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

        # We need to output a new list. So we need a dummy node
        dummy = Node()
        current = dummy
        l1 = list1.head
        l2 = list2.head

        # We are passed the list and we have the head so we can start at both heads and compare the two
        while l1 and l2:
            if l1.data <= l2.data:
                current.next = l1
                l1 = l1.next
                current = current.next
            else:
                current.next = l2
                l2 = l2.next
                current = current.next
            print(current.data)

        # Since the lists can be of different sizes, we need to add the remainder of the larger list at the end of current
        # this is obviously easy to do, but how to do it efficiently?
        # You can just add the list to the end without needing to iterate
        if l1:
            current.next = l1

        else:
            current.next = l2

        # So what are we returning?
        # We dont want the dummy, we want to start it from next
        # So send dummy.next

        temp = dummy.next
        while (temp): 
            print (temp.data, " -> ", end = '') 
            temp = temp.next
        print("")

        return dummy.next

        

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




    
    

