from collections import deque


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []
        queue = deque([])

        for idx, candidate in enumerate(candidates):
            queue.append([candidate, idx+1, [candidate]])

        while queue:
            currSum, idx, combination = queue.popleft()
            if currSum == target:
                combinations.append(tuple(combination))
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if currSum + candidates[i] <= target:
                    queue.append([currSum + candidates[i], i+1, combination + [candidates[i]]])
        return set(combinations)
