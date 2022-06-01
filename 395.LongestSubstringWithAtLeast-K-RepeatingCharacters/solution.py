"""
Logic:
    1.Calculate the frequency of each character and store it in a hashmap.
    2. Now think greedy that any character whose frequency is less than k, will never be a part of a valid substring.
    3. So whenever any such character is encountered(let's say at ith index) while iterating over the s, we could say that a valid substing might be present before (i-1)th index if not empty.
    4. We will partition our string on every such character encountered and check for the valid substring in that partition recursively and get the longest substring among all the partitions.
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s):
            return 0

        freq = {}
        for i, ch in enumerate(s):
            if ch not in freq:
                freq[ch] = 0
            freq[ch] += 1

        longSubstring = 0
        start = 0
        invalidSubstring = False
        for end in range(len(s)):
            if freq[s[end]] < k:
                longSubstring = max(longSubstring, self.longestSubstring(s[start:end], k))
                start = end+1
                invalidSubstring = True

        if not invalidSubstring:
            return len(s)
        else:
            return max(longSubstring, self.longestSubstring(s[start:], k))
