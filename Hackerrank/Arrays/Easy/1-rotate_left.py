class Solution(object):
    def rotate_left(self, a, d):
        for i in range(0, d):
            temp = a[0]
            for j in range(0, len(a) - 1):
                a[j] = a[j + 1]
                a[len(a) - 1] = temp
            return a

    def rotate_arr(self, arr, d):
        """
        Second solution
        """
        return arr[d:] + arr[:d]


print(Solution().rotate_left([1, 2, 3, 4, 5], 3))
