#!/usr/bin/python3
"""Is Unique

Question:
    Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?

"""


class Solution(object):
    """Finding the unique string in an element"""

    def is_unique_1(self, string):
        """Second solution using O(n^2) time complexity
        and O(n)

        Observation:
            Brute force - using nested loops

        """
        string = string.lower()
        for idx_1, str_1 in enumerate(string):
            for idx_2, str_2 in enumerate(string):
                if idx_1 == idx_2:
                    continue
                if str_1 == str_2:
                    return False
        return True

    def is_unique_2(self, string):
        """First solution"""
        if len(string) == len(set(string)):
            return True
        return False

    def is_unique_4(self, string):
        """Using a set"""
        char_seen = set()
        for character in string:
            if character in char_seen:
                return False
            else:
                char_seen.add(character)
        return True

    def is_unique_5(self, string):
        """Checks if a string is unique
        Time: O(n) | Space: O(n)

        Observation:
            Using a hash map

        """
        count = 0
        _map = {}
        for i in range(len(string)):
            if (string[i] == 'A' or string[i] == 'a'
                    or string[i] == 'Z' or string[i] == 'z'):
                continue
            if string[i] not in _map:
                _map[string[i]] = True
                count += 1
        if len(string) == len(_map):
            return True
        return False


string = "Helo"
print(Solution().is_unique_4(string))
