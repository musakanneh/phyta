#!/usr/bin/python3

class Solution(object):
    def character_replacement(self, s, k):
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
