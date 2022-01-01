#!/usr/bin/python3

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
