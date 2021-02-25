#!/usr/bin/python3


class Solution(object):
    """Longest Repeating Character Replacement
    Given a string s that consists of only uppercase English letters,
    you can perform at most k operations on that string.
    https://leetcode.com/problems/longest-repeating-character-replacement/

    """

    def character_replacement(self, s, k):
        """Use an empty string
        traverse the main string of letters
        and store update input string in the temp string.
        then return the length of the temp string

        """
        temp_string = ""
        count = 0
        for i in range(len(s)):
            while k:
                if s[i] == s[i + 1]:
                    temp_string.append(s[i])
                count += 1
        return len(temp_string)


characters = "ABAB"
k = 2
print(Solution().character_replacement(characters, k))
