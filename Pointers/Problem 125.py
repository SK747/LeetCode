"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""

## Easy solution: two pointers, one starts at the start, one at the end. Compare these two pointers at each step and return true if you 
## leave the loop without breaking
## Can iterate backwards either through for item in my_list[::-1]:
## or by using the built in reversed function
## Reversed is faster, [::-1] is more intuitive

class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i,j in zip(s.lower(),reversed(s.lower())):
            if i != j:
                return False
        return True
            

s = Solution()
print(s.isPalindrome('hmemh'))
        