class Solution:
    def dp(self, word, words, idx, lookup):
        if word[idx:] in words:
            return True

        if idx not in lookup:
            found = False
            for i in range(idx+1, len(word)+1):
                if word[idx:i] in words and self.dp(word, words, i, lookup):
                    found = True
                    break
            lookup[idx] = found
        return lookup[idx]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dp(s, wordDict, 0, {})
