from collections import deque


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        queue = deque([])

        for candidate in candidates:
            queue.append([candidate, [candidate]])

        while queue:
            currSum, combination = queue.popleft()
            if currSum == target:
                combinations.append(tuple(sorted(combination)))
            for candidate in candidates:
                if currSum + candidate <= target:
                    queue.append([currSum + candidate, combination+[candidate]])
        return set(combinations)
