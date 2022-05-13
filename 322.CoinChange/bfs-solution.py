from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        queue = deque([(amount, 0)])
        lookup = {amount}
        while queue:
            remainingAmount, coinsUsed = queue.popleft()
            if remainingAmount == 0:
                return coinsUsed
            for coin in coins:
                if remainingAmount - coin >= 0 and remainingAmount - coin not in lookup:
                    queue.append((remainingAmount - coin, coinsUsed + 1))
                    lookup.add(remainingAmount - coin)

        return -1
