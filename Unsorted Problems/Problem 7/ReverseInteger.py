"""Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned)."""

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        while x >= 1:
            digit = x % 10
            x = x // 10
            a = rev * 10 + digit
            rev = a
        return rev