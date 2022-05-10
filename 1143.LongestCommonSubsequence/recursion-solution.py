class Solution:
    def dpFn(self, a, b, lenA, lenB, i, j, dp):
        if dp[i][j] == -1:
            if i == lenA or j == lenB:
                dp[i][j] = 0
            elif a[i] == b[j]:
                dp[i][j] = 1 + self.dpFn(a, b, lenA, lenB, i + 1, j + 1, dp)
            else:
                dp[i][j] = max(self.dpFn(a, b, lenA, lenB, i + 1, j, dp), self.dpFn(a, b, lenA, lenB, i, j + 1, dp))
        return dp[i][j]

    def longestCommonSubsequence(self, a, b):
        lenA = len(a)
        lenB = len(b)
        dp = [[-1 for i in range(lenB + 1)] for j in range(lenA + 1)]
        self.dpFn(a, b, lenA, lenB, 0, 0, dp)
        return dp[0][0]


print(Solution().lcs("abc", "dbca"))
print(Solution().lcs("stone", "longest"))
print(Solution().lcs("edit", "distance"))
