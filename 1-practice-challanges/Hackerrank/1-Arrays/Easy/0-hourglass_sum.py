
class Solution(object):
    """
    """
    def hourglass_sum(self, arr):
        """
        """
        max_sum = -99
        for i in range(4):
            for j in range(4):
                top_sec = sum(arr[i][j: j + 3])
                mid_sec = arr[i + 1][j + 1]
                bot_sec = sum(arr[i + 2][j: j + 3])
                hourglass = top_sec + mid_sec + bot_sec
                max_sum = max(hourglass, max_sum)
        return max_sum

    def hourglass_sum_ii(self, arr):
        pass


matrix_array = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
print(Solution().hourglassSum(matrix_array))
