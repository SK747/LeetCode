"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true"""

class Solution(object):
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            
            elif s[i] == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False

            
            elif s[i] == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False

            else:
                stack.append(s[i])

            print(stack)
        if len(stack) == 0:
            return True
        else:
            return False
                    


s = Solution()
x = "()[]{}"
print(s.isValid(x))