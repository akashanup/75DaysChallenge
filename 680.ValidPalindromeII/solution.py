class Solution:
    def recur(self, s, start, end, deleted):
        if deleted > 1:
            return False
        if start >= end:
            return True
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return self.recur(s, start, end-1, deleted+1) or self.recur(s, start+1, end, deleted+1)
        return True

    def validPalindrome(self, s: str) -> bool:
        return self.recur(s, 0, len(s)-1, 0)
