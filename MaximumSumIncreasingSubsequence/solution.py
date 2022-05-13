class Solution:
    def maxSumIS(self, Arr, n):
        maxSum = [Arr[_] for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if Arr[j] < Arr[i] and maxSum[j] + Arr[i] > maxSum[i]:
                    maxSum[i] = maxSum[j] + Arr[i]
        return max(maxSum)
