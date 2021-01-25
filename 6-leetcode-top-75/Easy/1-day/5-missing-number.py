#!/usr/bin/python3


class Solution(object):
    """Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.

    https://leetcode.com/problems/missing-number/

    """

    def missing_number(self, nums):
        target_sum = sum(nums)
        n = len(nums)
        current_sum = n * (n + 1) // 2
        return int(current_sum - target_sum)


nums = [3, 0, 1]
print(Solution().missing_number(nums))
