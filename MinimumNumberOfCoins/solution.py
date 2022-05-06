import sys


class Solution:
    def dp(self, V, coins, i, lookup):
        if V < 0 or i == len(coins):
            return sys.maxsize
        if V == 0:
            return 0
        if (V, i) not in lookup:
            lookup[(V, i)] = min(1+self.dp(V-coins[i], coins, i, lookup), self.dp(V, coins, i+1, lookup))
        return lookup[(V, i)]

    def coinChange(self, V, coins):
        minCoins = self.dp(V, coins, 0, {})
        return minCoins if minCoins != sys.maxsize else -1


print(Solution().coinChange(30, [25, 10, 5]))
print(Solution().coinChange(2, [5]))
print(Solution().coinChange(11, [9, 6, 5, 1]))
print(Solution().coinChange(110, [9, 6, 5, 1]))
