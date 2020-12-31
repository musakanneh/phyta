from collections import Counter

class Solution(object):
    def sherlock_and_anagram(self, s):
        counter = 0
        dic = Counter(s)
        for i in range(2, len(s)):
            sub_string = s[0:i]
            sub_str_len = len(sub_string)
            dic["".join(sorted(sub_string))] += 1
            for j in range(1, len(s)):
                if j + sub_str_len <= len(s):
                    dic["".join(sorted(s[j:j+sub_str_len]))] += 1
        for key, val in dic.items():
            counter += val * (val - 1) //2
        return counter
_string = "abba"
print(Solution().sherlock_and_anagram(_string))