"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""


class Solution:
    """Valid Parentheses"""

    def isValid(self, s: str):
        openningBrackets = "({["
        clossingBrackets = ")}]"
        matchingBrackets = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in openningBrackets:
                stack.append(char)
            elif char in clossingBrackets:
                if len(stack) == 0:
                    return False
                if stack[-1] == matchingBrackets[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
