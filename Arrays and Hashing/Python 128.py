"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

## VERY IMPORTANT 
## "the numbers are stored in a HashSet (or Set, in Python) to allow O(1) lookups,"
## So we can use set(nums) and then just check the set to see if a certain number is there
## We can then add numbers to a new hashmap if they have no left number
## Then find if they have numbers to the right
