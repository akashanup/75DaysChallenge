class Solution:
    def integerBreak(self, n):
        dp = [0, 1]
        # Start from 2 to go till n.
        for m in range (2, n + 1):
            # For any number k between 2 to n,
            #   i equals to 1 and j equals to k-1 such that i+j = k
            # No increment i and decrement j and calculate the maxProduct for all possible combinations of i and j
            j = m - 1
            i = 1
            maxProduct = 0
            while i <= j:
                maxProduct = max(maxProduct, max(i, dp[i]) * max(j, dp[j]))
                j -= 1
                i += 1
            dp.append(maxProduct)
        return dp[n]
