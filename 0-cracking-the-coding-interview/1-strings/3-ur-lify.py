#!/usr/bin/python3

class URLify(object):
    def ur_lify(self, string, str_len):
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
