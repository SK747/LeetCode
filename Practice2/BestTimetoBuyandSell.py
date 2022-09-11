#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



class Solution(object):
    # This is such an easy question
    # We want to keep track of the maximum we can get as we iterate
    # To find the max we need to store the minumum and keep calculating maximums
    # If we find a new minimum, we replace our current min with that. Thats it

    def maxProfit(self, prices):
        max = 0
        min = prices[0]
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            if (prices[i]-min) > max:
                max = prices[i]-min
        return max


