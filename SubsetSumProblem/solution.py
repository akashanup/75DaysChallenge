class Solution:
    def dp(self, N, arr, amount, idx, lookup):
        if amount == 0:
            return True
        if amount < 0 or idx == N:
            return False
        if (amount, idx) not in lookup:
            lookup[(amount, idx)] = self.dp(N, arr, amount-arr[idx], idx+1, lookup) or self.dp(N, arr, amount, idx+1, lookup)
        return lookup[(amount, idx)]

    def isSubsetSum(self, N, arr, amount):
        return self.dp(N, arr, amount, 0, {})
