class Solution:
    MAPPING = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

    def recur(self, digits, i, combination):
        if i == len(digits):
            return [combination]
        combinations = []
        for ch in Solution.MAPPING[int(digits[i])]:
            combinations += (self.recur(digits, i+1, combination+[ch]))
        return combinations

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combinations = self.recur(digits, 0, [])
        return [''.join(combination) for combination in combinations]

