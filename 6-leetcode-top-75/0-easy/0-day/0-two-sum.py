#!/usr/bin/python3



class TwoNumberSum(object):
    """
    Two number sum
    Returns indices of two numbers such that they add up to target.
    https://leetcode.com/problems/two-sum/
    """

    def two_sum(self, nums, target):
        _hash_map = {}

        for i in range(len(nums)):
            result = target - nums[i]

            if result in _hash_map:
                return [_hash_map[result], i]

            _hash_map[nums[i]] = i
        return result[_hash_map]


nums = [2, 4, 6]
target = 10
print(TwoNumberSum().two_sum(nums, target))
