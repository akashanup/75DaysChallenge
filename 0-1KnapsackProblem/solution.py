import sys


class Solution:

    def dp(self, W, wt, val, n, i, lookup):
        if W < 0:
            return -sys.maxsize
        if W == 0 or i == n:
            return 0

        key = (W, i)
        if key not in lookup:
            lookup[key] = max(val[i] + self.dp(W - wt[i], wt, val, n, i + 1, lookup),
                              self.dp(W, wt, val, n, i + 1, lookup))
        return lookup[key]

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        return self.dp(W, wt, val, n, 0, {})
