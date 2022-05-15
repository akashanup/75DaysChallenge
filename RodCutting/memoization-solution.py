import sys


class Solution:
    def dp(self, n, prices, lookup):
        if n == 0:
            return 0
        if n == 1:
            return prices[0]
        if n not in lookup:
            maxCost = -sys.maxsize
            for i in range(1, n+1):
                maxCost = max(maxCost, prices[i-1]+self.dp(n-i, prices, lookup))
            lookup[n] = maxCost
        return lookup[n]

    def cutRod(self, price, n):
        return self.dp(n, price, {})


print(Solution().cutRod([1, 5, 8, 9, 10, 17, 17, 20], 8))
