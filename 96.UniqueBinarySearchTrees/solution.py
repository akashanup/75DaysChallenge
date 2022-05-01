class Solution:
    def numTrees(self, n: int) -> int:
        # Catlan Number
        # Base case is dp[0] is 1.
        dp = [1] + ([0] * n)
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[n]
