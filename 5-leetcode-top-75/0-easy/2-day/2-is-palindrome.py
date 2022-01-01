#!/usr/bin/python3

class Solution(object):
    def is_palindrome(self, s):
        result = [i for i in s.lower() if i.isalnum()]
        left, right = 0, len(result) - 1
        while left < right:
            if result[left] != result[right]:
                return False
            left += 1
            right -= 1
        return True


_input = "race a car"
print(Solution().is_palindrome(_input))
