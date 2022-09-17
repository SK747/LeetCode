class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == '+':
                x = int(stack.pop()) + int(stack.pop())
                stack.append(x)
                print(x,'+')
            elif tokens[i] == '-':
                x = -1* int(stack.pop()) + int(stack.pop())
                stack.append(x)
                print(x,'-')
            elif tokens[i] == '*':
                x = int(stack.pop()) * int(stack.pop())
                stack.append(x)
                print(x,'*')
            elif tokens[i] == '/':
                tmp = int(stack.pop())
                x = int(stack.pop()) // tmp
                stack.append(x)
                print(x,'/')
            else:
                stack.append(tokens[i])
            print(stack)
        
        return stack


s = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","-"]
print(s.evalRPN(tokens))