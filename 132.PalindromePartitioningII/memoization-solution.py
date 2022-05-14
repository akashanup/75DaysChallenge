import sys


class Solution:
    def isPalindrome(self, text):
        return text == text[::-1]

    def dp(self, text, i, j, lookup):
        if (i, j) not in lookup:
            # No cut is required if the text[i:j] is a palindrome.
            if self.isPalindrome(text[i:j]):
                lookup[(i, j)] = 0
            else:
                # Try to partition at all index and check:
                #   1. If the left part of partitioned string is palindrome then check for right part.
                #   2. If the left part of partitioned is not palindrome, try to partition at next index.
                #   3. Return the minimum number of partitioned required from above two steps.
                minCuts = sys.maxsize
                for k in range(i + 1, j):
                    if self.isPalindrome(text[i:k]):
                        minCuts = min(minCuts, 1 + self.dp(text, k, j, lookup))
                lookup[(i, j)] = minCuts
        return lookup[(i, j)]

    def minCut(self, s: str) -> int:
        return self.dp(s, 0, len(s), {})
