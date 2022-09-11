class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

    
    def PrintTreeBalanced(self):
        print(self.data)
        if self.left:
            self.left.PrintTreeBalanced()
        if self.right:
            self.right.PrintTreeBalanced()




root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(5)
root.insert(14)
root.insert(9)
root.PrintTreeBalanced()


class BstNode:

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def insert(self, key):
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = BstNode(key)
            else:
                self.right.insert(key)
        else: # self.key > key
            if self.left is None:
                self.left = BstNode(key)
            else:
                self.left.insert(key)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def value(self):
        print(b.key)

    ## This is preorder traversal
    def PrintTreeBalanced(self):
        print(self.key)
        if self.left:
            self.left.PrintTreeBalanced()
        if self.right:
            self.right.PrintTreeBalanced()


    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2



    # Now We want to invert a binary tree
    # Input: root = [12,3,5,6,9,14]
    # We are going to do DFS
    # Pre-order traversal. 
    # The only tricky part is how to deal with empty nodes

    def invertTree(self):

        # The only tricky part is how to deal with empty nodes
        # This checks where we are at before doing any recursion step or if statement
        if not self:
            return None

        temp = self.right
        self.right = self.left
        self.left = temp
        if self.right:
            self.right.invertTree()
        if self.left:
            self.left.invertTree()

    def lowestcommonancestor(self,p,q):
        print(self.key)
        if self.left == None or self.right == None:
            return False
        if (self.key >= p and self.key <= q) or (self.key >= q and self.key <= p):
            return self.key
        if (p > self.key and q > self.key):
            self.right.lowestcommonancestor(p,q)
        if (p < self.key and q < self.key):
            self.left.lowestcommonancestor(p,q)
        
            
        


import random

b = BstNode(20)
for _ in range(10):
    b.insert(random.randint(0, 40))
b.display()
b.value()
b.display()
print(b.lowestcommonancestor(4,22))




