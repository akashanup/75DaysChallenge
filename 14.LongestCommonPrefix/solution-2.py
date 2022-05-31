class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        minLen = len(min(strs, key=lambda x: len(x)))
        i = 0
        while i < minLen:
            j = 1
            while j < len(strs):
                if strs[j][i] != strs[j-1][i]:
                    break
                j += 1
            if j != len(strs):
                break
            i += 1
        return strs[0][:i]
