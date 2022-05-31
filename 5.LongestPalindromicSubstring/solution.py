class Solution:
    def checkPalindrome(self, s, backward, forward):
        while backward >= 0 and forward < len(s) and s[backward] == s[forward]:
            backward -= 1
            forward += 1
        return s[backward+1: forward]

    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            oddPalindromes = self.checkPalindrome(s, i, i)
            evenPalindromes = self.checkPalindrome(s, i, i+1)
            if len(oddPalindromes) > len(evenPalindromes):
                if len(oddPalindromes) > len(longest):
                    longest = oddPalindromes
            else:
                if len(evenPalindromes) > len(longest):
                    longest = evenPalindromes

        return longest

