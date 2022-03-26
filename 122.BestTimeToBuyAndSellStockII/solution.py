class Solution:
    def dp(self, prices, day, hasStock, lookup):
        # Base Case: No more stocks are available.
        if day == len(prices):
            return 0

        if (day, hasStock) not in lookup:
            if hasStock:
                # If I had stocks left from previous days then only I can sell it.
                activity = prices[day] + self.dp(prices, day+1, not hasStock, lookup)
            else:
                # If I don't have stocks left from previous days then only I can buy it.
                activity = -prices[day] + self.dp(prices, day+1, not hasStock, lookup)
            # I could also wish not to do anything on a day.
            noActivity = self.dp(prices, day+1, hasStock, lookup)
            # However, my maximum profit be the maximum of my activity performed or no activity.
            lookup[(day, hasStock)] = max(activity, noActivity)

        return lookup[(day, hasStock)]

    def maxProfit(self, prices: List[int]) -> int:
        return self.dp(prices, 0, 0, {})
