import sys


class Solution:
    def dp(self, arr, i, j, lookup):
        if (i == j):
            return 0

        if (i, j) not in lookup:

            ans = sys.maxsize

            for k in range(i, j):
                ans = min(ans,
                          self.dp(arr, i, k, lookup) + self.dp(arr, k + 1, j, lookup) + arr[i - 1] * arr[k] * arr[j])

            lookup[(i, j)] = ans
        return lookup[(i, j)]

    def matrixMultiplication(self, N, arr):
        return self.dp(arr, 1, N - 1, {})
