class Solution:
    def dp(self, prices, day, transactions, stocksInHand, lookup):
        if transactions >= 2 or day == len(prices):
            return 0
        key = (day, transactions, stocksInHand)
        if key not in lookup:
            if stocksInHand:
                # I can either hold the stock or sell the stocks.
                lookup[key] = max(self.dp(prices, day+1, transactions, True, lookup), prices[day]+self.dp(prices, day+1, transactions+1, False, lookup))
            else:
                # I can either buy the stocks or do nothing.
                lookup[key] = max(-prices[day]+self.dp(prices, day+1, transactions, True, lookup), self.dp(prices, day+1, transactions, False, lookup))
        return lookup[key]
        
    
    def maxProfit(self, prices: List[int]) -> int:
        return self.dp(prices, 0, 0, False, {}) 