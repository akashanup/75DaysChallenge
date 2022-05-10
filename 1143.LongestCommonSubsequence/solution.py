class Solution:
    def longestCommonSubsequence(self, a, b):
        lenA = len(a)
        lenB = len(b)
        dp = [[0 for i in range(lenB + 1)] for j in range(lenA + 1)]
        for i in range(1, lenA + 1):
            for j in range(1, lenB + 1):
                insertion = dp[i][j - 1]
                deletion = dp[i - 1][j]
                match = dp[i - 1][j - 1] + 1
                mismatch = dp[i - 1][j - 1]
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = max(insertion, deletion, match)
                else:
                    dp[i][j] = max(insertion, deletion, mismatch)
        return dp[lenA][lenB]
