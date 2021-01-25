#!/usr/bin/python3


class Solution:
    """Given an integer array nums, find the contiguous subarray
    (containing at least one number) which has the largest sum and return its sum.

    Example 1:
    -----------
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

    https://leetcode.com/problems/maximum-subarray/

    """

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, curr_sum = nums[0], 0
        for num in nums:
            curr_sum += num
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_sum
