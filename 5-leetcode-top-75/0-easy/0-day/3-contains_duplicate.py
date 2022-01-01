#!/usr/bin/python3


class Solution(object):
    def contains_duplicate(self, nums):
        hash_map = {}
        for n in nums:
            if n in hash_map:
                return True
            hash_map[n] = 1
        return False


num = [1, 2, 3, 4, 5, 6]
print(Solution().contains_duplicate(num))
