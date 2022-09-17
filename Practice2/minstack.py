class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val):
        self.stack.append(val)
        if not self.minstack or val < self.minstack[-1]:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])
        

    def pop(self):
       self.stack.pop()
       self.minstack.pop()
        

    def top(self):
        self.stack[-1]
        

    def getMin(self):
        print(self.minstack[-1])

    def printstack(self):
        print(self.stack)
        print(self.minstack)

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()
minStack.push(-3)
minStack.printstack()