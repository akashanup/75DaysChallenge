class Solution:
    def combinations(self, candidates, target, index, combination):
        if target < 0:
            return []
        if target == 0:
            return [combination]
        ans = []
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            ans += self.combinations(candidates, target - candidates[i], i + 1, combination + [candidates[i]])
        return ans

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.combinations(candidates, target, 0, [])
