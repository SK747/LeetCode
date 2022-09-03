## This is actually simple
## nums = [3,2,1,0,4]
## So here we will start at 3. We can jump 3, 2, or 1. We'll store our 3 jump and move 1
## At 2, we can now either jump 1 or 2. We also still have our 3 jump though, which has 2 left. So the two here is irrelevant. We can not ignore it
## At 1, we can jump once, but we still have one in our 3 jump, so this is also irrelevant. Ignore it.
## At 0. We cant move
## [2,3,1,1,4]
## At 2 we can jump 2 or 1
## Move to 3 (1 jump left). Here we can jump 1,2, or 3. The 1 jump left for 2 is irrelevant. Replace it with 3. 
## Move to 1. This is irrelevant. We have 2 left in our 3 jump.
## Move to 1. This is irrelevant, we have 1 left in our 3 jump.
## Move to 4. This index is the solution. We are done.

class Solution(object):
    def canJump(self, nums):
        jump = nums[0]

        # random edge case
        if len(nums) == 1:
            return True
    
        for i in range(len(nums)):
            jump = jump - 1
            if jump >= 0 and i == len(nums)-1:
                return True
            if jump < nums[i]:
                jump = nums[i]
            if jump == 0:
                return False
    
s = Solution()
print(s.canJump([3,2,1,0,4]))
        