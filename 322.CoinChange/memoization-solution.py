class Solution:
    def recur(self, coins, amount, lookup):
        if amount not in lookup:
            if amount == 0:
                return 0
            minCoins = sys.maxsize
            for coin in coins:
                if amount-coin >= 0:
                    minCoins = min(minCoins, 1 + self.recur(coins, amount-coin, lookup))
            lookup[amount] = minCoins
        return lookup[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = self.recur(coins, amount, {})
        return minCoins if minCoins != sys.maxsize else -1

