class Solution:
    def combinations(self, candidates, i, target, combination):
        if target < 0:
            return []
        if target == 0:
            return [combination]

        combinations = []
        if i < len(candidates):
            combinations = self.combinations(candidates, i, target-candidates[i], combination+[candidates[i]]) + self.combinations(candidates, i+1, target, combination)
        return combinations

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.combinations(candidates, 0, target, [])
