class Pangram(object):
    def __init__(self):
        pass

    def is_pangram(self, s):
        _list = []
        for letter in s:
            if letter.isalpha():
                _list.append(letter.lower())
        is_alpha = []
        for letter in range(97, 123):
            is_alpha.append(chr(letter))
        for letter in _list:
            if letter in is_alpha:
                is_alpha.append(letter)
        return "Is Pangram" if len(is_alpha) == 0 else "Not Pangram"

    def is_pangram_ii(self, string):
        pass


_string = "abcdefghijklmnopqrstuvwxyz"
print(Pangram().is_pangram(_string))
