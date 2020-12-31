class Solution(object):
    def two_sum_ii(self, nums, target):
        _hash_map = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in _hash_map:
                return [_hash_map[res], i]
            _hash_map[nums[i]] = i
        return res[_hash_map]

    def remove_duplicate(self, nums):
        left, right = 0, 0
        counter = 1
        for right in range(len(nums)):
            if nums[right] != nums[left]:
                left += 1
                counter += 1
                nums[left] = nums[right]
        return counter

    def max_sub_array(self, nums):
        """
        find the contiguous subarray (containing at least one number) 
        which has the largest sum and return its sum.
        """
        max_sum = nums[0]
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum

    def plus_one(self, digits):
        """
        Given a non-empty array of decimal digits representing 
        a non-negative integer, increment one to the integer.
        """
        list_len = len(digits)
        for num in reversed(range(list_len)):
            digits[num] += 1
            if digits[num] < 10:
                return digits
            digits[num] = 0
        digits.insert(0, 1)
        return digits

    def merge(self, nums1, nums2):
        pass

# Plus one sub array
_digits = [1, 2, 3]
print(Solution().plus_one(_digits))

# Maximum sub array
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(Solution().max_sub_array(nums))

# Remove dublicate number
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# print(Solution().remove_duplicate(nums))

# Two number sum
nums = [2, 7, 11, 15]
target = 9
# print(Solution().two_sum_ii(nums, target))
