#!/usr/bin/python3


class Solution(object):
    """
    Finds if the array contains any duplicates.
    Returns true if any value appears at least twice in the array,
    False - if every element is distinct.
    https://leetcode.com/problems/contains-duplicate/
    """

    def contains_duplicate(self, nums):
        """
        Args:
            nums(List[int]): list of input integers

        """
        hash_map = {}
        for n in nums:
            if n in hash_map:
                return True
            hash_map[n] = 1
        return False


num = [1, 2, 3, 4, 5, 6]
print(Solution().contains_duplicate(num))
