class Solution:
    def computeLPS(self, pat, lps):
        l = 0
        lps[0] = 0
        i = 1
        while i < len(pat):
            if pat[i] == pat[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l > 0:
                    l = lps[l-1]
                else:
                    lps[i] = 0
                    i += 1

    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)
        self.computeLPS(needle, lps)
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == len(needle):
                return i-j
            elif i < len(haystack) and haystack[i] != needle[j]:
                if j > 0:
                    j = lps[j-1]
                else:
                    i += 1
        return -1

