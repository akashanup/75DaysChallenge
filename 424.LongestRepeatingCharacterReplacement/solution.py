class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        start, end = 0, 0
        maxLen = 0
        maxCount = 0
        while end < len(s):
            # Store the count of each character in the current window
            if s[end] in hashmap:
                hashmap[s[end]] += 1
            else:
                hashmap[s[end]] = 1

            """
                Check whether the current window has utilized 'k' changes:
                    1. If yes, then slide the window by one position i.e, start becomes start+1 and the count of character at start index decreases by 1.
                    2. If no, then update maxLen if window size is greater than maxLen
                In the current window, 'k' changes has been done or not can be checked by knowing te window size and maximum count of any charcter in the window as:
                (end-start+1) - maxCount > k
            """
            windowSize = end-start+1
            maxCount = max(maxCount, hashmap[s[end]])
            if windowSize - maxCount > k:
                hashmap[s[start]] -= 1
                start += 1
            else:
                maxLen = max(maxLen, windowSize)
            end += 1
        return maxLen

