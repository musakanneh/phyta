class Solution:
    """Given an array of integers, find if the array contains any duplicates.

    Your function should return true if any value appears at least twice in the array,
    and it should return false if every element is distinct.
    
    https://leetcode.com/problems/contains-duplicate/
    
    """

    def containsDuplicate(self, nums: List[int]):
        hash_map = {}
        for n in nums:
            if n in hash_map:
                return True
            hash_map[n] = 1
        return False
