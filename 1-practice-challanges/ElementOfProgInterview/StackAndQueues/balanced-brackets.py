def is_balanced(s):
    brackets = {"{": "}", "[": "]", "(": ")"}
    stack = []
    for char in s:
        if char in ["{", "[", "("]:
            stack.append(char)
        else:
            if stack:
                top = stack.pop()
                if brackets[top] != char:
                    return "No"
            else:
                return "No"
    return "NO" if stack else "YES"


s = "{{[[(())]]}}"
print(is_balanced(s))
