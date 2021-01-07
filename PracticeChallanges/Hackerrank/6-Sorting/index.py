class Solution(object):
    def bobble_sort(self, a):
        swap_element = 0
        for i in range(len(a) - 1, 0, -1):
            for j in range(i):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swap_element += 1
        print("Array is sorted in {} swaps.".format(swap_element))
        print("First Element: {}".format(a[0]))
        print("Last Element: {}".format(a[i]))
    
    def max_toys(self, prices, k):
        count = 0
        prices = sorted(prices)
        for i in range(len(prices)):
            k = k - prices[i]
            if k < 0:
                break
            count += 1
        return count

class Player(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        pass

    def comparator(self, a, b):
        if a.score > b.score:
            return -1
        elif  a.score < b.score:
            return 1
        elif a.score == b.score:
            if a.name > b.name:
                return 1
            elif a.name < b.name:
                return -1
            return 0

_prices = [1, 12, 5, 111, 200, 1000, 10]
k = 50
print(Solution().max_toys(_prices, k))

_swaps = [6, 4, 1]
# print(Solution().bobble_sort(_swaps))
