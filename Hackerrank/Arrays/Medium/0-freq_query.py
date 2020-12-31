from collections import Counter


class Solution(object):
    def freq_query(self, queries):
        """
        Return frequency of occurances of 
        element in an array
        """
        result = []
        hash_map = Counter()
        hash_values = Counter()
        for ops, val in queries:
            if ops == 1:
                hash_values[hash_map[val]] -= 1
                hash_map[val] += 1
                hash_values[hash_map[val]] += 1
            elif ops == 2:
                if hash_map[val] > 0:
                    hash_values[hash_map[val]] -= 1
                    hash_map[val] -= 1
                    hash_values[hash_map[val]] += 1
            else:
                result.append(1 if hash_values[val] == 0 else 0)
        return result


_queries = [(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]
print(Solution().freq_query(_queries))
