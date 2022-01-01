#!/usr/bin/python3

class Solution(object):
    def is_anagram(self, s, t):

        hash_map = {}

        for char in s:
            if char not in hash_map:
                hash_map[char] = 0
            hash_map[char] += 1

        for char in t:
            if char not in hash_map:
                hash_map[char] = 0
            hash_map[char] -= 1

        for key in hash_map.keys():
            if hash_map[key] != 0:
                return False

        return True
