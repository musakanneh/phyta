#!/usr/bin/python3
"""Longest Substring Without Repeating Characters"""


class Solution(object):
    """Two number sum

    Question:
        Given a string s, find the length of the longest
        substring without repeating characters.

        Example 1:
        -----------------------------
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

        Example 2:
        ----------------------------
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

        Example 3:
        ---------------------------
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    """

    def length_of_longest_substring(self, s):
        """Length of the longest substring"""
        hash_map = {}
        left = 0
        right = 0
        n = len(s)
        ans = 0

        while left < n and right < n:
            el = s[right]
            if el in hash_map:
                left = max(left, hash_map[el] + 1)
            hash_map[el] = right
            ans = max(ans, right - left + 1)
            right += 1

        return ans


s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
