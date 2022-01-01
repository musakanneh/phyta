#!/usr/bin/python3

class Solution(object):
    def string_builder(self, words):
        sentence = " "
        for w in words:
            sentence += w
        return sentence

    def solution_2(self, words):
        sentence = " "
        for w in words:
            sentence.append(w)
        return sentence


print(Solution().solution_2("This is a sentence"))
