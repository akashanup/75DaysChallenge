class Solution:
    def combinations(self, candidates, target, i, combination):
        if target == 0:
            return [combination]
        if target < 0 or i >= len(candidates):
            return []
        ans = []
        ans += self.combinations(candidates, target - candidates[i], i + 1, combination + [candidates[i]])
        if i == 0:
            ans += self.combinations(candidates, target, i + 1, combination)
        else:
            # To optimize for duplicate calls
            j = i+1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
                j = i
            ans += self.combinations(candidates, target, j, combination)

        return ans

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = self.combinations(candidates, target, 0, [])
        return set([tuple(_) for _ in ans])
