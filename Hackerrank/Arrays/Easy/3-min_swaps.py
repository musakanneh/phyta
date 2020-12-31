class Solution(object):
    def min_swaps(self, arr):
        counter = 0
        temp = [0]*len(arr)
        for index, value in enumerate(arr):
            temp[value - 1] = index
            for i in range(len(arr)):
                if arr[i] != i + 1:
                    t = temp[i]
                    arr[i], arr[t] = t + 1, arr[i]
                    temp[i], temp[arr[t] - 1] = i, t
                    counter += 1
        return counter


arr_elem = [4, 3, 1, 5, 2]
print(Solution().min_swaps(arr_elem))
