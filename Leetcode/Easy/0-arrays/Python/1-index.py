class Solution(object):
    def generate(self, num_rows):
        result = []
        if num_rows == 1:
            return [[1]]
        for i in range(1, num_rows + 1):
            row = [1]
            for j in range(1, i):
                last_row = row[len(row) - 1]
                row.append(last_row * (i - j) // j)
            result.append(row)
        return result

    def max_profit(self, prices):
        if prices == 0:
            return 0
        result = 0
        for i in range(len(prices)):
            minimum = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            result = max(result, prices[i] - minimum)
        return result

    def max_prifit_ii(self, prices):
        if not prices:
            return 0
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
        return profit

    def first_disappeared_number(self, nums):
        missing_val = []
        for n in nums:
            pos = abs(n) - 1
            if nums[pos] > 0:
                nums[pos] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                missing_val.append(i + 1)
        return missing_val


nums_input = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().first_disappeared_number(nums_input))

_input = [7, 2, 4, 3, 5, 3, 10, 4]
# print(Solution().max_prifit_ii(_input))

_input = [7, 2, 4, 3, 5, 3, 10, 4]
# print(Solution().max_profit(_input))

nums_rows = 5
# print(Solution().generate(nums_rows))
