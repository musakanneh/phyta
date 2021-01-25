#!/usr/bin/python3
"""URLify

Question:
    Write a method to replace all spaces in a string with '%20'. You may assume that the string
    has sufficient space at the end to hold the additional characters, and that you are given the "true"
    length of the string. (Note: If implementing in Java, please use a character array so that you can
    perform this operation in place.)
    
    Input: "Mr John Smith ", 13
    
    Output: "Mr%20John%20Smith"

"""


class URLify(object):
    def ur_lify(self, string, str_len):
        """Replace all spaces in a string

        Args:
            string(str): string input
            str_len(int): len of the string,
            not considering the last empty spaces

        Complexity analysis:
            Time: O(n)
            Space: O(n)

        """
        new_string = ""
        for i in range(len(string)):
            if string[i] == " ":
                new_string += "%20"
            else:
                new_string += string[i]
        return new_string


string = "Mr John Smith"
str_len = 13
print(Solution().ur_lify(string, str_len))
