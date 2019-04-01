## December 9th 2018
## Leetcode Q.122


class Solution(object):
    def maxProfit(self, prices):
        return sum([price2 - price1 for price1, price2 in zip(prices, prices[1:]) if price2 - price1 > 0]) ## ZIP creates a tuple list