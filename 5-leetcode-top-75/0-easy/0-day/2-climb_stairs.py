#!/usr/bin/python3


class Solution(object):
    """
    Climbing Stairs
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps.
    In how many distinct ways can you climb to the top?
    https://leetcode.com/problems/climbing-stairs/
    """

    def climb_stairs(self, n):
        """
        Args:
            n(int): integer input
        """
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # _map = {1: 1, 2: 2}
        # for i in range(3, n + 1):
        #     curr = _map[i - 1] + _map[i + 2]
        #     _map[i] = curr
        # return _map[n]

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
