class Solution:
    def combinations(self, nums, k, i, combination):
        if len(combination) == k:
            return [combination]
        ans = []
        if i < len(nums):
            ans = self.combinations(nums, k, i+1, combination+[nums[i]]) + self.combinations(nums, k, i+1, combination)
        return ans

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [_ for _ in range(1, n+1)]
        return self.combinations(nums, k, 0, [])
