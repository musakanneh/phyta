def largest_pectangle(h):
    stack = []
    area = i = 0
    h.append(0)
    while i < len(h):
        if not stack or h[stack[-1]] < h[i]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            area = max(area, h[top] * (i - stack[-1] - 1 if stack else i))
    return area


h = [1, 2, 3, 4, 5]
print(largest_pectangle(h))
