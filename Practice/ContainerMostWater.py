class Solution(object):
    def maxArea(self, height):
        l,r,water,maximum = 0,len(height)-1,0,0
        while l < r:
            water = max(height[l],height[r])*(r-l)
            if water > maximum:
                maximum = water
            if height[l] > height[r]:
                r = r - 1
            if height[l] <= height[r]:
                l = l + 1
        return maximum

            

        

s = Solution()
arr1 = [1,3,8,6,2,5,4,8,3,7,4]

print(s.maxArea(arr1))
