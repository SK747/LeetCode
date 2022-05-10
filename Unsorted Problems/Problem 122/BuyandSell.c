/* 

Date: December 9th 2018

Leetcode Q.122


Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

*/

#include <stdio.h>


int maxProfit(int* prices, int pricesSize);



int main() {
    int nums[]={7,1,5,3,6,4};
    
    int profit = maxProfit(nums, 6);
    
    printf("%d",profit)

    return 0;
}

/*
 * Function:  maxProfit
 * --------------------
 *  calculate maximum possible profit from array representing stock prices
 *
 *  prices: The array passed to function
 *  pricesSize: THe size of the array
 *
 *  returns: the maximum profit as an int
 */

int maxProfit(int* prices, int pricesSize) {
	int profit = 0;
	int x, y;

	for (x = 0; x < pricesSize; x++) { /* navigate until you find the local peak */
		if ((prices[x+1]-prices[x]) > 0) {
			profit = prices[x+1] - prices[x] + profit
		}
	}
	return profit
}
