## write a function that checks whether the braces in each string are correctly matched
## prints 1 to standard output (stdout) if the braces in each string are matched and 0 if they're not (one result per line)

class Solution:
    def CheckBraces(self, arr):
        stack = []
        retarray = []
        for j in range(len(arr)):
            if arr[j] == '{' or arr[j] == '[' or arr[j] == '(':
                stack.append(arr[j])
            
            if arr[j] == '}' or arr[j] == ']' or arr[j] == ')':
                stack.append(arr[j])
                print('temp stack is', stack)
                print('arr j is', arr[j])
                print('stack -1 is', stack[-1])
                if stack[-2] == '{' and arr[j] == '}':
                    stack.pop()
                    stack.pop()
                elif stack[-2] == '(' and arr[j] == ')':
                    stack.pop()
                    stack.pop()
                elif stack[-2] == '[' and arr[j] == ']':
                    stack.pop()
                    stack.pop()
            print(stack)
        if len(stack) == 0:
            return True
        else:
            return False

s = Solution()
print(s.CheckBraces(']'))
                
