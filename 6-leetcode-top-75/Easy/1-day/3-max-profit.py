#!/usr/bin/python3


"""Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a 
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""


class Solution(object):
    def max_profit(self, prices):
        if not prices:
            return 0
        result = 0
        for i in range(len(prices)):
            mini_val = prices[0]
        for j in range(1, len(prices)):
            if prices[j] < mini_val:
                mini_val = prices[j]
            else:
                result = max(result, prices[j] - mini_val)
        return result


prices = [7, 1, 5, 3, 6, 4]
print(Solution().max_profit(prices))
