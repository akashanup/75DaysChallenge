class Solution:
    def permutations(self, unprocessed, processed):
        if not unprocessed:
            return [processed]
        ans = []
        for i in range(len(processed)+1):
            ans += self.permutations(unprocessed[1:], processed[:i]+[unprocessed[0]]+processed[i:])
        return ans

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        return self.permutations(nums, [])
