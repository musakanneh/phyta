# """
# reorder entry - from even to odd
# O(n) time | O(1) space
# """
# class Solution(object):
#     def reorder_entry(self, array):
#         even_num, odd_num = 0, len(array) - 1
#         while even_num < odd_num:
#             if array[even_num] % 2 == 0:
#                 even_num += 1
#             array[even_num], array[odd_num] = array[odd_num], array[odd_num]
#             odd_num -= 1
#         return array
# # print(Solution().reorder_entry([1, 3, 2, 6, 4, 5]))

# """
# dutch flag pertitioning
# """
# class Solution(object):
#     def partion_dutch_flag(self, pivot_num, array):
#         pivot = array[pivot_num]
#         less, equal, greater = 0, 0, len(array)
#         while equal < greater:
#             if array[equal] < pivot:
#                 array[less], array[equal] = array[equal], array[less]
#                 less, equal = less + 1, equal + 1
#             elif array[equal] == pivot:
#                 equal += 1
#             else:
#                 greater -= 1
#                 array[equal], array[greater] = array[greater], array[equal]
#         return array
# print(Solution().partion_dutch_flag(3, [1, 3, 2, 6, 4, 5]))





def arr_len(a, b):

    len_1 = len(a)
    len_2 = len(b)

    if len_1 == len_2:
        return True
    return False

a = [1, 2, 3, 4]
b = [1, 3, 4, 4, 10]
print(arr_len(a, b))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

for row in matrix:
    for num in row:
        if not all(type(num) in [int, float:
            raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
