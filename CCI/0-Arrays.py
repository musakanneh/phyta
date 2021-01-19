class Arrays:
    """A class representation of an array
    """

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
            Check for occurences of characters
            in the array

        """
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
        """Finds the first non-repeating character
        in it and return its index. If it doesn't exist,
        return -1.

        Args:
            string(str): the input string

        """
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


# print(Arrays().string_builder("This is a sentence"))
# print(Arrays().first_uniq_char("loveleetcode"))
print(Arrays().is_unique("letcod"))
