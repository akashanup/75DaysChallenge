class Solution:
    def editDistance(self, s, t):
        lenS = len(s)
        lenT = len(t)
        dp = [[None for i in range(lenT + 1)] for j in range(lenS + 1)]
        for i in range(lenS + 1):
            dp[i][0] = i
        for i in range(lenT + 1):
            dp[0][i] = i
        for i in range(1, lenS + 1):
            for j in range(1, lenT + 1):
                insertion = 1 + dp[i][j - 1]
                deletion = 1 + dp[i - 1][j]
                mismatch = 1 + dp[i - 1][j - 1]
                match = dp[i - 1][j - 1]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = min(insertion, deletion, match)
                else:
                    dp[i][j] = min(insertion, deletion, mismatch)
        return dp[lenS][lenT]
