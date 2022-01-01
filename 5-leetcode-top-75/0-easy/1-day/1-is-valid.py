#!/usr/bin/python3

class Solution:
    def is_valid(self, s: str):
        opening_brackets = "({["
        clossing_brackets = ")}]"
        matching_brackets = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in opening_brackets:
                stack.append(char)
            elif char in clossing_brackets:
                if len(stack) == 0:
                    return False
                if stack[-1] == matching_brackets[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


brackets = "()[]{}"
print(Solution().is_valid(brackets))
