import sys


class Solution:
    def cutRod(self, price, n):
        lookup = [0 for _ in range(n + 1)]
        lookup[0] = 0

        for i in range(1, n + 1):
            maxPrice = -sys.maxsize
            for j in range(i):
                maxPrice = max(maxPrice, price[j] + lookup[i - j - 1])
            lookup[i] = maxPrice

        return lookup[n]
