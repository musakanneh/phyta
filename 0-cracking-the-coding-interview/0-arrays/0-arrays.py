#!/usr/bin/python3


class Arrays:
    """A class representation of an array"""

    def string_builder(self, words):
        """Apprends two strings"""
        sentence = " "
        for w in words:
            sentence += w
        return sentence

    def is_unique(self, string):
        """Determines if a string hasall
        unique characters

        Approach:
            Create a map and look it up
            Check for occurences of characters in the array"""
        _map = {}
        for i in range(len(string)):
            if string[i] not in _map:
                _map[string[i]] = 1
            else:
                _map[string[i]] += 1
        for i in range(len(string)):
            if _map[string[i]] > 1:
                return "Not unique"
        return "Unique"

    def first_uniq_char(self, string):
        """Finds the first non-repeating character in it and
        return its index. If it doesn't exist, return -1.

        Args:
            string(str): the input string"""
        _hash_map = {}
        for i in range(len(string)):
            if string[i] not in _hash_map:
                _hash_map[string[i]] = 1
            else:
                _hash_map[string[i]] += 1
        for i in range(len(string)):
            if _hash_map[string[i]] == 1:
                return i
        return -1

    def check_permutation(self, string):
        """Given two strings, write a method to
        decide if one is a permutation of the other

        Args:
            string(str): input string"""
        pass

    def url_lify(self, string):
        """Replaces all spaces in a string with '%20'. You may assume
        that the string has sufficient space at the end to hold the additional
        characters, and that you are given the "true" length of the string.
        (Note: If implementing in Java, please use a character array so that you
        can perform this operation in place.)"""
        pass

    def palindrome_permutation(self, string):
        """A function to check if it is a permutation of a palin­drome."""
        pass

    def check_inclusion(self, s1, s2):
        """LeetCode: Given two strings s1 and s2, write a function
        to return true if s2 contains the permutation of s1.
        In other words, one of the first string's permutations is
        the substring of the second string.

        Approach:
            Sort the strings

        """
        n1 = len(s1)
        n2 = len(s2)
        a, b = sorted(s1), sorted(s2)

    def max_sum(self, _array, num, k):
        pass


# print(Arrays().string_builder("This is a sentence"))
# print(Arrays().first_uniq_char("loveleetcode"))
# print(Arrays().is_unique("letcod"))
s1 = "ab"
s2 = "eidbaooo"
print(Arrays().check_inclusion(s1, s2))
