#!/usr/bin/python3

class Arrays:
    def string_builder(self, words):
        sentence = " "
        for w in words:
            sentence += w
        return sentence

    def is_unique(self, string):
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
        pass

    def url_lify(self, string):
        pass

    def palindrome_permutation(self, string):
        pass

    def check_inclusion(self, s1, s2):
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
