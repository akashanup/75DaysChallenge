class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # Calculate postfix max to determine what is the maximum price of stack after the ith day
        postfixMax = [0] * n
        pMax = prices[n-1]
        for i in range(n-2, -1, -1):
            pMax = max(pMax, prices[i+1])
            postfixMax[i] = pMax

        maxProfit = 0
        for i in range(n):
            maxProfit = max(maxProfit, postfixMax[i] - prices[i])

        return maxProfit if maxProfit >= 0 else 0
