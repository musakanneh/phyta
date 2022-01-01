from collections import Counter


class StringManipulations(object):
    def __init__(self):
        pass

    def make_anagram(self, a, b):
        _dic_a = Counter(a)
        _dic_b = Counter(b)
        total_count = (_dic_a - _dic_b) + (_dic_b - _dic_a)
        return sum(total_count.values())

    def make_anagram_ii(self, a, b):
        _map = Counter(a)
        for c in b:
            _map[c] -= 1
        value = _map.values()
        _sum = sum(abs(i) for i in value)
        return _sum

    def alternating_characters(self, s):
        count = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
        return count

    def reverse_string(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

    def first_uniq_char(self, s):
        _map = {}
        for i in range(len(s)):
            if s[i] not in _map:
                _map[s[i]] = 1
            else:
                _map[s[i]] += 1
        for i in range(len(s)):
            if _map[s[i]] == 1:
                return i
        return -1
