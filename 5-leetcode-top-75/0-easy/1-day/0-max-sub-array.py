#!/usr/bin/python3

class Solution(object):
    def max_sub_array(self, nums):
        max_sum, curr_sum = nums[0], 0
        for num in nums:
            curr_sum += num
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().max_sub_array(nums))
