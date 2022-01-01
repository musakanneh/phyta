#!/usr/bin/python3

class Solution(object):
    def climb_stairs(self, n):
        temp = {0: 1, 1: 2}
        for i in range(2, n):
            temp[i] = temp[i-1] + temp[i-2]
        return temp[n-1]

    def fibonacci(self, n):
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)


n = 4
print(Solution().fibonacci(n))
