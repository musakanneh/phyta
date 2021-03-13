#!/usr/bin/python3

class MaximumSubArray:
    """
    Class for finding the maximum of numbers
    within an array
    """

    def max_sub_array(self, arr):
        """
        Trackboth current and max sums
        subtract it from the first element
        then, traverse the the array and
        return the maximum sum
        """
        current_sum = 0
        for i in range(len(arr)):
            max_sum = arr[i]
        return max_sum


arr = [1, 2, 3, 4, 5, 6, 7]
print(MaximumSubArray().max_sub_array(arr))
