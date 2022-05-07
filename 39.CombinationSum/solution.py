class Solution:
    def recur(self, candidates, target, temp, combinations):
        if target == 0:
            combinations.add(tuple(sorted(temp)))

        for candidate in candidates:
            if candidate <= target:
                self.recur(candidates, target - candidate, temp + [candidate], combinations)
        return combinations

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.recur(candidates, target, [], set())
