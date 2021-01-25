#!/usr/bin/python3

class Solution:
    """Valid Palindrome
    Given a string, determine if it is a palindrome,
    considering only alphanumeric characters and ignoring cases.

    https://leetcode.com/problems/valid-palindrome/

    Example 1:

    Input: "A man, a plan, a canal: Panama"
    Output: true
    """

    def isPalindrome(self, s: str):
        result = [i for i in s.lower() if i.isalnum()]
        left, right = 0, len(result) - 1
        while left < right:
            if result[left] != result[right]:
                return False
            left += 1
            right -= 1
        return True
