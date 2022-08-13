class Solution(object):
    def maxProfit(self, prices):
        ## So here we want to find the maximum profit we can get from ONE trade
        ## And then we want to return the maximum money we can get
        ## This is pretty straightforward... We have two pointers
        ## We basically move them according to basic logic. If the profit is negative move both over by one
        ## if its positive, move right pointer by one
        ## This will allow us to find minimums
        l, r = 0,1
        maximum = 0
        while r < len(prices):
            if prices[r]-prices[l] < 0:
                l += 1
            if prices[r]-prices[l] >= 0:
                if prices[r]-prices[l] > maximum:
                    maximum = prices[r] - prices[l]
                r += 1
        return maximum



        

           

s = Solution()
arr1 = [5,1,3,4,2,7,7,5,8]

print(s.maxProfit(arr1))
