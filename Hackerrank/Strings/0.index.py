from collections import Counter


class StringManipulations(object):
    def __init__(self):
        pass

    def make_anagram(self, a, b):
        """
        1st solution
        """
        _dic_a = Counter(a)
        _dic_b = Counter(b)
        total_count = (_dic_a - _dic_b) + (_dic_b - _dic_a)
        return sum(total_count.values())

    def make_anagram_ii(self, a, b):
        """
        2nd solution
        """
        _map = Counter(a)
        for c in b:
            _map[c] -= 1
        value = _map.values()
        _sum = sum(abs(i) for i in value)
        return _sum

    def alternating_characters(self, s):
        """
        Delete zero or more characters
        in the string.
        """
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
        """
        Given a string, find the first non-repeating
        character in it and return its index.
        If it doesn't exist, return -1.
        """
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

    def is_palindrome(self, s):
        result = [i for i in s.lower() if i.isalnum()]
        left, right = 0, len(result) - 1
        while left < right:
            if result[left] != result[right]:
                return False
            left += 1
            right -= 1
        return True


s = "race a car"
print(StringManipulations().is_palindrome(s))
