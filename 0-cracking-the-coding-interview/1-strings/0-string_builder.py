#!/usr/bin/python3
"""String builder"""


class Solution(object):
    def string_builder(self, words):
        """Apprends two strings

        Args:
             words(str): words inputs

        """
        sentence = " "
        for w in words:
            sentence += w
        return sentence

    def solution_2(self, words):
        """Solution two"""
        sentence = " "
        for w in words:
            sentence.append(w)
        return sentence


print(Solution().solution_2("This is a sentence"))
